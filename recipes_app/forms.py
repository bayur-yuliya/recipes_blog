from django import forms

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
