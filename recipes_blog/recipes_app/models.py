from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.TextField(blank=True)
    recipe_text = models.TextField(blank=True)
    cooking_time = models.CharField(max_length=30, blank=True, null=True)
    quantity_of_servings = models.PositiveIntegerField(blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
