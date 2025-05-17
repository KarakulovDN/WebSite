from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from pages.models import Product
from .forms import ProductForm
from django.views.generic import TemplateView

from django.core.paginator import Paginator


class HomeView(TemplateView):
    template_name = 'pages/home.html'

def catalog(request):
    return render(request, 'pages/catalog.html')

class ContactsView(TemplateView):
    template_name = 'pages/contacts.html'

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



