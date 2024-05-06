from django.db import models
from django.contrib.auth.models import User

# Extendar den inbyggda Auth Usern.
# Fält som definieras här tillhör den skapade användaren.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

class Building(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Essentials:
    name_of_asset = models.CharField(max_length=255)
    full_asset_address = models.TextField()
    address_line1 = models.CharField(max_length=255)
    postcode_zip_code = models.CharField(max_length=50)
    town_city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    # Optionals:
    asset_description = models.TextField(null=True)
    year_built = models.IntegerField(null=True, blank=True)
    year_built_specific = models.CharField(max_length=255, null=True, blank=True)
    most_recent_major_refurbishment = models.IntegerField(null=True, blank=True)
    address_line2 = models.CharField(max_length=255, null=True, blank=True)
    address_line3 = models.CharField(max_length=255, null=True, blank=True)
    address_line4 = models.CharField(max_length=255, null=True, blank=True)
    county_region = models.CharField(max_length=255, null=True, blank=True)
    asset_manager_name = models.CharField(max_length=255, null=True, blank=True)
    asset_ownership_name = models.CharField(max_length=255, null=True, blank=True)
    asset_tenancy_manager_name = models.CharField(max_length=255, null=True, blank=True)
    asset_occupier_name = models.CharField(max_length=255, null=True, blank=True)
    breeam_assessment_organisation_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name_of_asset
    

# Exempelvis "Health and Wellbeing" som innehåller Hea01-Hea13
class Category(models.Model):
    name = models.CharField(max_length=255)

class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='questions', null=True)
    prompt = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True, null=True)  # Ensure this is unique across the database

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=255)
    score = models.IntegerField(default=0)

class BuildingResponse(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='responses')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)  # To track when the response was made

    

