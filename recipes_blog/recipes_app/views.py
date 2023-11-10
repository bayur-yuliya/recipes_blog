from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from .models import Recipe


def index(request):

    recipes = Recipe.objects.all()
    data = {
        "title": "Главная страница",
        "recipes": recipes,
    }
    return render(request, "recipes_app/index.html", context=data)


def about(request):
    return render(request, "recipes_app/about.html", {"title": "О нас"})


def add_page(request):
    return HttpResponse("Добавить статью")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Войти")


def post(request, recipe_id):
    recipes = Recipe.objects.get(id=recipe_id)
    data = {"data": recipes}
    return render(request, "recipes_app/post.html", context=data)


def show_categories(request, cat_id):
    return index(request)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена. </h1>")
