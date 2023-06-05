from django.shortcuts import render, redirect
from django.views import View

from .models import Product, Comment


# def home(request):
#     products = Product.objects.all()
#     return render(request, 'index.html', {'products': products})
class HomeView(View):

    def get(self, request):
        products = Product.objects.all()
        comments = Comment.objects.all()
        return render(request, 'index.html', {
            'products': products,
            'comments': comments
        })

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        comment = Comment.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        comment.save()
        return redirect('/')


def about(request):
    return render(request, 'about.html')


def product(request):
    return render(request, 'product.html')