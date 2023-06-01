from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    #categories
    path('addcategory',views.add_category,name="addcategory"),
    path('editcategory/<cid>',views.edit_category,name="editcategory"),
    path('editcategory',views.edit_category,name="editcategory"),
    path('categories',views.get_categories,name="categories"),
    path('categories/delete/<cid>',views.delete_category,name="deletecategory"),
    #units
    path('addunit',views.add_unit,name="addunit"),
    path('editunit/<uid>',views.edit_unit,name="editunit"),
    path('editunit',views.edit_unit,name="editunit"),
    path('units',views.get_units,name="units"),
    path('units/delete/<uid>',views.delete_unit,name="deleteunit"),
    #ingredients
    path('addingredient', views.add_ingredient, name="addingredient"),
    path('editingredient/<iid>', views.edit_ingredient, name="editingredient"),
    path('editingredient', views.edit_ingredient, name="editingredient"),
    path('ingredients', views.get_ingredients, name="ingredients"),
    path('ingredients/delete/<iid>', views.delete_ingredient, name="deleteingredient"),
    #recipes
    path('addrecipe', views.add_recipe, name="addrecipe"),
    path('editrecipe/<rid>', views.edit_recipe, name="editrecipe"),
    path('editrecipe', views.edit_recipe, name="editrecipe"),
    path('recipes', views.get_user_recipes, name="recipes"),
    path('recipes/delete/<rid>', views.delete_recipe, name="deleterecipe"),
    path('allrecipes',views.all_recipes,name='allrecipes'),
    path('recipes/details/<rid>',views.recipe_details,name="recipedetails"),
    #recipe_ingredient
    path('addingredienttorecipe/<rid>',views.add_ingredient_to_recipe,name="addingredienttorecipe"),
    path('editrecipeingredient/<rid>',views.edit_recipe_ingredient,name="editrecipeingredient"),
    path('deleterecipeingredient/<rid>',views.delete_recipe_ingredient,name="deleterecipeingredient"),
    #users
    path('login', views.user_login),
    path('register', views.register, name='register'),
    path('logout',views.logout_user,name='logout')
]