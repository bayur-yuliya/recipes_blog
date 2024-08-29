from django.core.management.base import BaseCommand

from recipes_app.models import Recipe


class Command(BaseCommand):
    help = """the command generates a recipes"""

    def handle(self, *args, **options):
        Recipe.objects.create(
            title="Шарлотка",
            ingredients="Яблоки, Мука, яица, сахар",
            recipe_text="Приготовьте все ингредиенты для шарлотки. "
            "Включите разогреваться духовку до 180 градусов. "
            "Начните приготовление пирога с начинки. Возьмите 3 яблока, помойте, "
            "очистите от кожуры, удалите семена и плодоножку. "
            "Нарежьте сначала на дольки, а потом на кусочки одинакового размера. "
            "По желанию можете не срезать кожуру.",
            cooking_time="30 мин",
            quantity_of_servings=4,
            is_published=1,
            slug="sharlotka",
        )

        self.stdout.write(self.style.SUCCESS("Все прошло успешно!"))
