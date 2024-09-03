from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Recipe


class RecipeForm(forms.ModelForm):
    title = (forms.CharField(max_length=100),)
    ingredients = (forms.CharField(widget=forms.Textarea),)
    recipe_text = (forms.CharField(widget=forms.Textarea),)
    cooking_time = forms.CharField(max_length=100)
    quantity_of_servings = forms.IntegerField()
    is_published = forms.BooleanField()
    slug = forms.SlugField()

    class Meta:
        model = Recipe
        fields = (
            "title",
            "ingredients",
            "recipe_text",
            "cooking_time",
            "quantity_of_servings",
            "slug",
        )


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Username", required=True)
    email = forms.EmailField(label="Email address", required=True)
    password1 = forms.CharField(label="Password", required=True)
    password2 = forms.CharField(label="Password confirmation", required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
