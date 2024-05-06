
from django import forms
from django.forms import ModelForm, inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Building, Choice

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class BuildingBasicsForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ['name_of_asset', 'full_asset_address', 'address_line1', 'postcode_zip_code', 'town_city', 'country']



class ChoiceForm(forms.Form):
    choice = forms.ModelChoiceField(queryset=Choice.objects.none(), empty_label=None, widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        question_id = kwargs.pop('question_id', None)
        super().__init__(*args, **kwargs)
        if question_id:
            self.fields['choice'].queryset = Choice.objects.filter(question_id=question_id)