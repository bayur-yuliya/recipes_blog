from django.urls import path, register_converter

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
    path("category/<int:cat_id>/", views.show_categories, name="show_categories"),
]
