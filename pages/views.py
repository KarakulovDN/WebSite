from django.shortcuts import render
from pages.models import Product


def home(request):
    """
    Отображение главной страницы с последними 5 добавленными продуктами
    """
    # Получаем последние 5 продуктов, отсортированных по дате создания (новые первыми)
    latest_products = Product.objects.order_by('-created_at')[:5]

    # Для отладки выводим в консоль
    print("Последние 5 продуктов:")
    for product in latest_products:
        print(f"- {product.name} (Цена: {product.price}, Категория: {product.category.name})")

    # Формируем контекст для шаблона
    context = {
        'title': 'Главная страница',
        'products': latest_products,
        'products_count': len(latest_products),
    }

    return render(request, 'pages/home.html', context)


def catalog(request):
    return render(request, 'pages/catalog.html')

def contacts(request):
    return render(request, 'pages/contacts.html')

def category(request):
    return render(request, 'pages/category.html')