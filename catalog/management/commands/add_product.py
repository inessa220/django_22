from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add test product to the database"

    def handle(self, *args, **kwargs):
        # Удаление существующих данных
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создание категорий
        one = Category.objects.create(name="1", description="11")
        two = Category.objects.create(name="Напитки")

        # Создание продуктов
        product1 = Product.objects.create(
            name="Тест1", description="Описание1", category=one, price=10
        )
        product2 = Product.objects.create(
            name="Тест2", description="Описание2", category=two, price=100
        )

        self.stdout.write(self.style.SUCCESS("Successfully added test products"))
