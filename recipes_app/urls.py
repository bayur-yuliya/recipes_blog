from django.urls import path, register_converter

from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("add_page/", views.add_page, name="add_page"),
    path("edit_recipe/<int:pk>", views.edit_recipe, name="edit_recipe"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.login, name="login"),
    path("recipe/<int:pk>/", views.post, name="recipe"),
    path("ingredients/<int:ingredient>/", views.ingredients, name="ingredients"),
    path(
        "ingredients/<slug:ingredient_slug>/",
        views.ingredients_by_slug,
        name="ingredients_by_slug",
    ),
    path("archive/<year4:year>/", views.archive, name="archive"),
    path("category/<int:category_id>/", views.category, name="category"),
    path("category/", views.categories_list, name="categories_list"),
]
