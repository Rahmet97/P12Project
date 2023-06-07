from django.shortcuts import render, redirect
from django.views import View

from .forms import CommentForm
from .models import Product, Comment


# def home(request):
#     products = Product.objects.all()
#     return render(request, 'index.html', {'products': products})
class HomeView(View):

    def get(self, request):
        form = CommentForm()
        products = Product.objects.all()
        comments = Comment.objects.all()
        return render(request, 'index.html', {
            'products': products,
            'comments': comments,
            'form': form
        })

    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            message = form.cleaned_data.get('message')

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