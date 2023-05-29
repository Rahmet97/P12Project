from django.urls import path
from .views import home, about, product

urlpatterns = [
    path('', home),
    path('about', about),
    path('product', product),
]