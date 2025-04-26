from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def catalog(request):
    return render(request, 'pages/catalog.html')

def contacts(request):
    return render(request, 'pages/contacts.html')

def category(request):
    return render(request, 'pages/category.html')