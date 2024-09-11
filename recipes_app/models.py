from django.db import models
from django.urls import reverse


class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Recipe.Status.PUBLISHED)


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Recipe(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, "Черновик"
        PUBLISHED = 1, "Опубликовано"

    title = models.CharField(max_length=255)
    ingredients = models.TextField(blank=True)
    recipe_text = models.TextField(blank=True)
    cooking_time = models.CharField(max_length=30, blank=True, null=True)
    quantity_of_servings = models.PositiveIntegerField(blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.PUBLISHED)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    objects = models.Manager()
    published = PublishManager()

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ["-time_create"]
        indexes = [models.Index(fields=["-time_create"])]

    def get_absolute_url(self):
        return reverse("recipe", kwargs={"recipe_slug": self.slug})
