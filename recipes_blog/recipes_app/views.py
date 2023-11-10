from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


data_db = [
    {'id': 1, 'title': 'Apple pie', "ingredients": "Apples, eggs, flour", 'time': "1 hour", "quantity_of_servings": 4,
     "is_published": True},
    {'id': 2, 'title': 'Cherry pie', "ingredients": "Cherry, eggs, flour", 'time': "1 hour", "quantity_of_servings": 4,
     "is_published": False},
    {'id': 3, 'title': 'Pear pie', "ingredients": "Pears, eggs, flour", 'time': "1 hour", "quantity_of_servings": 4,
     "is_published": True},
]


def index(request):
    data = {
        "title": "Главная страница",
        "menu": menu,
        'data_db': data_db,
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


def post(request, post_id):
    data = {"data": post_id}
    return render(request, "recipes_app/post.html", context=data)


def show_categories(request, cat_id):
    return index(request)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена. </h1>")
