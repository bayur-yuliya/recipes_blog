from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound, HttpResponse

from .forms import RegisterUserForm
from .models import Recipe


def index(request):
    recipes = Recipe.published.all()
    data = {
        "title": "Главная страница",
        "recipes": recipes,
    }
    return render(request, "recipes_app/index.html", context=data)


def about(request):
    return render(request, "recipes_app/about.html", {"title": "О нас"})


def add_page(request):
    return render(request, "recipes_app/add_page.html", {"title": "Добавиление статьи"})


def contact(request):
    return render(request, "recipes_app/contact.html", {"title": "Обратная связь"})


def login(request):
    if request.method == "GET":
        form = RegisterUserForm()
        return render(request, "register/login.html", {"form": form})

    form = RegisterUserForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, "register/login.html", {"form": form})


def post(request, recipe_slug):
    recipes = get_object_or_404(Recipe, slug=recipe_slug)
    data = {"data": recipes}
    return render(request, "recipes_app/post.html", context=data)


def ingredients(request, ingredient):
    return HttpResponse(f"<h1> Поиск по id ингридиентов {ingredient} </h1>")


def ingredients_by_slug(request, ingredient_slug):
    return HttpResponse(
        f"<h1> Поиск по ингридиентам, через slug {ingredient_slug} </h1>"
    )


def archive(request, year):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"Архив рецептов за {year} год")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена. </h1>")
