from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import *

# Create your views here.


def home(request):
    return render(request, 'home.html')

def login_page(request):
    return render(request, 'login_page.html')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    user_buildings = Building.objects.filter(user=request.user)
    return render(request, 'profile.html', {'user': user, 'user_buildings': user_buildings})


@login_required
def add_building(request):
    if request.method == 'POST':
        form = BuildingBasicsForm(request.POST)
        if form.is_valid():
            building = form.save(commit=False)
            building.user = request.user  # Associate the building with the current user
            building.save()
            return redirect('profile')  # Redirect to profile page after adding building
    else:
        form = BuildingBasicsForm()
    return render(request, 'add_building_basics.html', {'form': form})

@login_required
def building_profile(request, building_id):
    building = get_object_or_404(Building, id=building_id)
    categories = Category.objects.all()

    for category in categories:
        questions = Question.objects.filter(category=category)
        responses = BuildingResponse.objects.filter(building=building, question__in=questions)
        total_score = sum(response.choice.score for response in responses)
        # Assign the score directly to the category object for simplicity
        category.total_score = total_score

    return render(request, 'building_profile.html', {
        'building': building,
        'categories': categories
    })



@login_required
def category_detail(request, building_id, category_id):
    building = get_object_or_404(Building, id=building_id)
    category = get_object_or_404(Category, id=category_id)
    questions = Question.objects.filter(category=category)

    # Fetch all responses for this building and this category of questions
    answered_questions_ids = BuildingResponse.objects.filter(
        building=building,
        question__in=questions
    ).values_list('question_id', flat=True).distinct()

    return render(request, 'category_detail.html', {
        'building': building,
        'category': category,
        'questions': questions,
        'answered_questions_ids': answered_questions_ids
    })


@login_required
def question_detail(request, building_id, category_id, question_code):
    building = get_object_or_404(Building, id=building_id)
    question = get_object_or_404(Question, code=question_code)
    choices = question.choices.all()

    if request.method == 'POST':
        choice_id = request.POST.get('choice')
        if choice_id:
            choice = get_object_or_404(Choice, id=choice_id)
            # Create or update the response
            BuildingResponse.objects.update_or_create(
                building=building,
                question=question,
                defaults={'choice': choice}
            )
            return redirect('category_detail', building_id=building_id, category_id=category_id)  # Redirecting to the building profile or another appropriate view

    return render(request, 'question_detail.html', {
        'building': building,
        'question': question,
        'choices': choices
    })

