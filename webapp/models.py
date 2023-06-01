from django.contrib.auth.models import User
from django.db import models

class Unit(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=5,decimal_places=2)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey('Recipe',on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    count = models.DecimalField(max_digits=5,decimal_places=2)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    img = models.CharField(max_length=500)

    def __str__(self):
        return self.name



