from django.urls import path, register_converter, re_path

from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("add_page/", views.add_page, name="add_page"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.login, name="login"),
    path("recipe/<slug:recipe_slug>/", views.post, name="recipe"),
    path("ingredients/<int:ingredient>/", views.ingredients, name="ingredients"),
    path(
        "ingredients/<slug:ingredient_slug>/",
        views.ingredients_by_slug,
        name="ingredients_by_slug",
    ),
    re_path(r"archive/(?P<year>[0-9]{4})/", views.archive, name="archive"),
]
