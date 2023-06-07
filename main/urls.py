from django.urls import path
from .views import HomeView, about, product, Contact

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', about),
    path('product', product),
    path('contact', Contact.as_view(), name='contact')
]