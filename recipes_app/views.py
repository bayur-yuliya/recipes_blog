from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.core.paginator import Paginator

from .forms import RegisterUserForm, RecipeForm
from .models import Recipe, Category


def index(request):
    recipes = Recipe.published.filter(is_published=True)
    paginator = Paginator(recipes, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    data = {
        "title": "Главная страница",
        "recipes": recipes,
        "page_obj": page_obj,
    }
    return render(request, "recipes_app/index.html", context=data)


def login(request):
    if request.method == "GET":
        form = RegisterUserForm()
        return render(request, "register/login.html", {"form": form})

    form = RegisterUserForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, "register/login.html", {"form": form})


def categories(request):
    categories = Category.objects.all()
    return render(
        request, "recipes_app/categories.html", context={"categories": categories}
    )


def add_page(request):
    if request.method == "GET":
        form = RecipeForm()
        return render(request, "recipes_app/add_page.html", {"form": form})
    form = RecipeForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, "recipes_app/add_page.html", {"form": form})


def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "GET":
        form = RecipeForm(instance=recipe)
        return render(request, "recipes_app/edit_recipe.html", {"form": form})
    form = RecipeForm(request.POST, instance=recipe)
    if form.is_valid():
        form.save()
    return render(request, "recipes_app/edit_recipe.html", {"form": form})


def post(request, recipe_slug):
    recipes = get_object_or_404(Recipe, slug=recipe_slug)
    data = {"data": recipes}
    return render(request, "recipes_app/post.html", context=data)


def contact(request):
    return render(request, "recipes_app/contact.html", {"title": "Обратная связь"})


def about(request):
    return render(request, "recipes_app/about.html", {"title": "О нас"})


def ingredients(request, ingredient):
    return HttpResponse(f"<h1> Поиск по id ингридиентов {ingredient} </h1>")


def ingredients_by_slug(request, ingredient_slug):
    return HttpResponse(
        f"<h1> Поиск по ингридиентам, через slug {ingredient_slug} </h1>"
    )


def archive(request, year):
    if year > 2024:
        uri = reverse("ingredients_by_slug", args=("apple",))
        return redirect(uri)
    return HttpResponse(f"Архив рецептов за {year} год")


def page_not_found(request, exception):
    return render(request, "page_not_found/page_not_found.html")
