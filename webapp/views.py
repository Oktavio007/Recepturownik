from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from webapp.forms import CategoryForm, UnitForm, IngredientForm, RecipeForm, CustomUserCreationForm, \
    RecipeIngredientForm

# Create your views here.
from webapp.models import Category, Unit, Ingredient, Recipe, RecipeIngredient

# funkcja zwraca główną strone aplikacji
def index(request):
    return render(request,'index.html')

#======================================================== Categories ========================================================

# funkcja zwraca widok ze wszystkimi kategoriami przepisu, widok dostepny dla administratorta
@login_required()
def get_categories(request):
    if request.user.is_staff:
        categories = Category.objects.all()
        return render(request, 'categories.html', {'categories': categories})
    else:
        return redirect('/')
# funkcja obsługująca wyswietlenie formularza kategorii i zapis danych z formularza do bazy
# (widok dla administratora)
@login_required()
def add_category(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = CategoryForm(request.POST)
            form.save()
            return redirect('/categories')
        else:
            form = CategoryForm()
            return render(request, 'category.html', {'form': form})
    return redirect('/')
# edycja funkcja obsługująca wyswietlenie formularza kategorii, edycja i zapis danych z formularza
@login_required()
def edit_category(request,cid):
    if request.user.is_staff:
        category = get_object_or_404(Category, pk=cid)

        if request.method == "POST":
            form = CategoryForm(request.POST,instance=category)
            form.save()
            return redirect('/categories')
        else:
            form = CategoryForm(instance=category)
            return render(request, 'edit_category.html', {'form': form, 'category': category })
    else:
        redirect('/')
# funkcja obsługujaca usuwanie kategorii
@login_required()
def delete_category(request,cid):
    if request.user.is_staff:
        Category.objects.filter(id=cid).delete()
        return redirect('/categories')
    else:
        return redirect('/')


#======================================================== Units ========================================================
# funkcja zwraca widok ze wszystkimi jednostkami, widok dostepny dla administratorta
@login_required()
def get_units(request):
    if request.user.is_staff:
        units = Unit.objects.all()
        return render(request, 'units.html', {'units': units})
    else:
        return redirect('/')
# funkcja bsługująca wyswietlenie formularza jednostki, dodawanie i zapis danych z formularza
@login_required()
def add_unit(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = UnitForm(request.POST)
            form.save()
            return redirect('/units')
        else:
            form = UnitForm()
            return render(request, 'unit.html', {'form': form})
    return redirect('/')
# funkcja bsługująca wyświetlenie formularza jednostki, edycja i zapis danych z formularza
@login_required()
def edit_unit(request,uid):
    if request.user.is_staff:
        unit = get_object_or_404(Unit, pk=uid)

        if request.method == "POST":
            form = UnitForm(request.POST, instance=unit)
            form.save()
            return redirect('/units')
        else:
            form = UnitForm(instance=unit)
            return render(request, 'edit_unit.html', {'form': form, 'unit': unit})
    else:
        redirect('/')
# # funkcja bsługująca usuwanie jednostki
@login_required()
def delete_unit(request,uid):
    if request.user.is_staff:
        Unit.objects.filter(id=uid).delete()
        return redirect('/units')
    else:
        return redirect('/')

#======================================================== Ingredients ========================================================
# funkcja zwraca widok ze wszystkimi składnikami, widok dostepny dla administratorta
@login_required()
def get_ingredients(request):
    if request.user.is_staff:
        ingredients = Ingredient.objects.all()
        return render(request, 'ingredients.html', {'ingredients': ingredients})
    else:
        return redirect('/')
# funkcja bsługująca wyswietlenie formularza ze składnikami, dodawanie i zapis danych z formularza
@login_required()
def add_ingredient(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = IngredientForm(request.POST)
            form.save()
            return redirect('/ingredients')
        else:
            form = IngredientForm()
            return render(request, 'ingredient.html', {'form': form})
    return redirect('/')
# funkcja bsługująca wyświetlenie formularza ze składnikami, edycja i zapis danych z formularza
@login_required()
def edit_ingredient(request,iid):
    if request.user.is_staff:
        ingredient = get_object_or_404(Ingredient, pk=iid)

        if request.method == "POST":
            form = IngredientForm(request.POST, instance=ingredient)
            form.save()
            return redirect('/ingredients')
        else:
            form = IngredientForm(instance=ingredient)
            return render(request, 'edit_ingredient.html', {'form': form, 'ingredient': ingredient})
    else:
        redirect('/')
# funkcja bsługująca usuwanie składników
@login_required()
def delete_ingredient(request,iid):
    if request.user.is_staff:
        Ingredient.objects.filter(id=iid).delete()
        return redirect('/ingredients')
    else:
        return redirect('/')

#======================================================== Recipes ========================================================
# funkcja zwraca widok ze wszystkimi przepisami uzytkownika
@login_required()
def get_user_recipes(request):
    recipes = Recipe.objects.filter(user=request.user).all()
    return render(request, 'recipes.html', {'recipes': recipes})

# funkcja bsługująca wyswietlenie formularza z przepisem dodawanie i zapis danych z formularza
@login_required()
def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        w = form.save(commit=False)
        w.user = get_object_or_404(User, id=request.user.id)
        w.save()
        return redirect('/recipes')
    else:
        form = RecipeForm()
        return render(request, 'recipe.html', {'form': form})
# funkcja bsługująca wyświetlenie formularza z przepisem, edycja i zapis.
@login_required()
def edit_recipe(request,rid):
    recipe = get_object_or_404(Recipe, pk=rid)

    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        w = form.save(commit=False)
        w.user = get_object_or_404(User, id=request.user.id)
        w.save()
        return redirect('/recipes')
    else:
        form = RecipeForm(instance=recipe)
        return render(request, 'edit_recipe.html', {'form': form, 'recipe': recipe})

# usuwanie przepisu
@login_required()
def delete_recipe(request,rid):
    Recipe.objects.filter(id=rid).delete()
    return redirect('/recipes')

# widok z wszystkimi przepisami
def all_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'allrecipes.html', {'recipes': recipes})
# zwraca widok ze szczegółami przepisu
def recipe_details(request,rid):
    recipe = get_object_or_404(Recipe, id=rid)
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)

    cost = round(sum([ingredient.count * ingredient.ingredient.cost for ingredient in ingredients]),2)

    return render(request,"recipe_details.html",{'recipe': recipe, 'ingredients': ingredients, 'cost': cost })


#======================================================== RecipeIngredients ========================================================
# zwraca formularz do dodawania składnika do przepisu i zapisuje dane do bazy
@login_required()
def add_ingredient_to_recipe(request,rid):
    recipe = get_object_or_404(Recipe, id=rid)

    if recipe.user == request.user:
        if request.method == "POST":
            form = RecipeIngredientForm(request.POST)
            form.save()
            return redirect('/recipes/details/' + str(rid))
        else:
            form = RecipeIngredientForm(initial={'recipe': recipe})
            return render(request,'add_ingredient_to_recipe.html',{ 'form': form, 'rid': rid, 'recipe': recipe })
    else:
        return redirect('/')
# edycja składnika w ramach przepisu i zapis do bazy
@login_required()
def edit_recipe_ingredient(request,rid):
    recipe_ingredient = get_object_or_404(RecipeIngredient, pk=rid)

    if request.method == "POST":
        form = RecipeIngredientForm(request.POST, instance=recipe_ingredient)
        w = form.save(commit=False)
        w.user = get_object_or_404(User, id=request.user.id)
        w.save()
        return redirect('/recipes/details/' + str(w.recipe.id))
    else:
        print("rc: " + str(recipe_ingredient.count))
        form = RecipeIngredientForm(instance=recipe_ingredient)
        return render(request, 'edit_recipe_ingredient.html', {'form': form, 'recipeingredient': recipe_ingredient})
# usuwanie składnika z przepisu
@login_required()
def delete_recipe_ingredient(request,rid):
    recipe_ingredient = get_object_or_404(RecipeIngredient, pk=rid)
    ri_id = recipe_ingredient.recipe.id
    RecipeIngredient.objects.filter(id=rid).delete()
    return redirect('/recipes/details/' + str(ri_id))


#======================================================== Users ========================================================
# formularz logowania i sprawdzenie danych użytkownika, zalogowanie do aplikacji
def user_login(request):
    if request.method == "POST":
        username = request.POST["login"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(request, 'login.html')
        else:
            login(request, user)
            return redirect('/')
    else:
        return render(request, 'login.html')
# formularz rejestracji uzytkownika i zapis danych użytkownika do bazy
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})
# wylogowanie uzytkownika
def logout_user(request):
    logout(request)
    return redirect('/login')


