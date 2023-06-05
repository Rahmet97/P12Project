from django.urls import path
from .views import HomeView, about, product

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', about),
    path('product', product),
]