from django.core.management.base import BaseCommand

from recipes_app.models import Recipe, Category


class Command(BaseCommand):
    help = """the command generates a recipes"""

    def handle(self, *args, **options):
        categories = ("Суп", "Десерт", "Закуска")
        recipes = (
            (
                "Шарлотка",
                "4 яблока,160 г муки, 20 г сливочного масла, 4 яйца, 150 г сахара",
                "45 мин",
                4,
                1,
                "sharlotka1",
                Category.objects.get(id=2),
            ),
            (
                "Кабачки по-корейски",
                "1 средний кабачок, 1 средняя морковь, 1 ч. л. соли, 1 ч. л. сахар",
                "15 мин",
                4,
                1,
                "kabachki-po-korejski",
                Category.objects.get(id=3),
            ),
            (
                "Абрикосовое варенье",
                "1 кг абрикосов, 500 г сахара, 100 г миндальных хлопьев",
                "30 мин",
                1,
                1,
                "abrikosovoe-varene-s-mindalem",
                Category.objects.get(id=2),
            ),
        )
        for category in categories:
            Category.objects.create(name=category)

        for recipe in recipes:
            Recipe.objects.create(
                title=recipe[0],
                ingredients=recipe[1],
                recipe_text="recipe_text",
                cooking_time=recipe[2],
                quantity_of_servings=recipe[3],
                is_published=recipe[4],
                slug=recipe[5],
                category_id=recipe[6],
            )

        self.stdout.write(self.style.SUCCESS("Все прошло успешно!"))
