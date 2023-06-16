from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CommentForm
from .models import Product, Comment
from django.db.models import Q
from datetime import datetime, timedelta
from django.utils import translation


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
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})

def remote(request):
    return render(request, 'remot.html')

def video(request):
    return render(request, 'video.html')


class Contact(LoginRequiredMixin, View):
    def get(self,request):
        return render(request, 'contact.html')

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        msg = f'''
{message}

Full name: {name}
email: {email}
phone number: {phone}
                    '''

        send_mail(
            'Yangi habar',
            msg,
            name,
            ['rahmetruslanov6797@gmail.com'],
            fail_silently=True
        )
        return redirect('contact')


class ProductDetail(View):

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'product-detail.html', {'product': product})
