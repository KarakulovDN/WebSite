from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from pages.models import Product
from .forms import ProductForm

from django.core.paginator import Paginator


def home(request):
    product_list = Product.objects.all().order_by('-created_at')
    paginator = Paginator(product_list, 6)  # 6 товаров на странице

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pages/home.html', {'page_obj': page_obj})

def catalog(request):
    return render(request, 'pages/catalog.html')

def contacts(request):
    return render(request, 'pages/contacts.html')

def category(request):
    return render(request, 'pages/category.html')

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'pages/product_detail.html', {'product': product})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()

    return render(request, 'pages/add_product.html', {'form': form})



