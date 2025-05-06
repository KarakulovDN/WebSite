from django.core.management.base import BaseCommand
from pages.models import Category, Product
from django.core.files import File
import os
from django.conf import settings


class Command(BaseCommand):
    help = 'Загружает тестовые данные в базу'

    def handle(self, *args, **options):
        self.stdout.write("Удаление старых данных...")
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write("Создание категорий...")
        categories = [
            {"name": "Электроника", "description": "Гаджеты и техника"},
            {"name": "Одежда", "description": "Модная одежда"},
            {"name": "Книги", "description": "Литература разных жанров"},
        ]

        created_categories = []
        for cat_data in categories:
            cat = Category.objects.create(**cat_data)
            created_categories.append(cat)
            self.stdout.write(f"Создана категория: {cat.name}")

        self.stdout.write("Создание продуктов...")
        products = [
            {
                "name": "Смартфон",
                "price": 599.99,
                "description": "Новый флагманский смартфон",
                "category": created_categories[0],
                "image": "products/smartphone.jpg"
            },
            {
                "name": "Ноутбук",
                "price": 1299.99,
                "description": "Мощный игровой ноутбук",
                "category": created_categories[0],
                "image": "products/laptop.jpg"
            },
            {
                "name": "Джинсы",
                "price": 49.99,
                "description": "Стильные мужские джинсы",
                "category": created_categories[1],
                "image": "products/jeans.jpg"
            },
        ]

        for prod_data in products:
            image_path = prod_data.pop('image', None)
            product = Product.objects.create(**prod_data)

            if image_path:
                full_path = os.path.join(settings.MEDIA_ROOT, image_path)
                if os.path.exists(full_path):
                    with open(full_path, 'rb') as img_file:
                        product.image.save(
                            os.path.basename(image_path),
                            File(img_file),
                            save=True
                        )

            self.stdout.write(f"Создан продукт: {product.name}")

        self.stdout.write(
            self.style.SUCCESS("Тестовые данные успешно загружены!")
        )