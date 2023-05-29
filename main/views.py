from django.shortcuts import render

from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def about(request):
    return render(request, 'about.html')


def product(request):
    return render(request, 'product.html')