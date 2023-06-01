from django import forms
from django.contrib.auth.forms import UserCreationForm

from webapp.models import Category, Recipe, Ingredient, Unit, RecipeIngredient

# formularz do wypełnieniach danych kategirii przepisu
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['id', 'name']

    id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
# formularz do wpisywania danych dot. jednostki miary
class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['id', 'name']

    id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
# formularz do wpisywania danych dot. składnika
class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['id','name', 'cost', 'unit']

    #unit = forms.ModelChoiceField(queryset=Unit.objects.all(), empty_label=None, label='Jednostka')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dodaj atrybuty dla pól formularza (opcjonalne)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['cost'].widget.attrs.update({'class': 'form-control'})
        self.fields['unit'].widget.attrs.update({'class': 'form-control'})

# formularz dot. przepisu
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["name","description","category","img"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dodaj atrybuty dla pól formularza (opcjonalne)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['img'].widget.attrs.update({'class': 'form-control'})
# formularz do rejestracji uzytkownika
class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
# formularz do dodawania składników do przepisu
class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'recipe', 'count', 'unit']
        widgets = { 'recipe': forms.HiddenInput() }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dodaj atrybuty dla pól formularza (opcjonalne)
        self.fields['ingredient'].widget.attrs.update({'class': 'form-control'})
        self.fields['count'].widget.attrs.update({'class': 'form-control'})
        self.fields['unit'].widget.attrs.update({'class': 'form-control'})