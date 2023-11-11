from django.db import models
from django.urls import reverse


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.TextField(blank=True)
    recipe_text = models.TextField(blank=True)
    cooking_time = models.CharField(max_length=30, blank=True, null=True)
    quantity_of_servings = models.PositiveIntegerField(blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('recipe', kwargs={"recipe_slug": self.slug})
