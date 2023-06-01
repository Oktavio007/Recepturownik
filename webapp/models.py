from django.contrib.auth.models import User
from django.db import models
# klasa modelu przechowująca dane o jednostkach miary
class Unit(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# przechowyjąca dane o składnikach
class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=5,decimal_places=2)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.name
# klasa modelu przechowuje dane o kategoriach dań
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
# klasa łącząca składnik z przepisem przechowuje dane przepisu, składnika i jego ilośc
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey('Recipe',on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    count = models.DecimalField(max_digits=5,decimal_places=2)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
# klasa przechowuje dane przepisu
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    img = models.CharField(max_length=500)

    def __str__(self):
        return self.name



