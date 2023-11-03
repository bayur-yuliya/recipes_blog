from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


menu = [
    {"title": "Добавить статью", "url_name": "add_page"},
    {"title": "Обратная связь", "url_name": "contact"},
    {"title": "Войти", "url_name": "login"},
]


def index(request):
    data = {
        "title": "Главная страница",
        "menu": menu,
    }
    return render(request, "recipes_app/index.html", context=data)


def about(request):
    return render(request, "recipes_app/about.html", {"title": "О нас", "menu": menu})


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
