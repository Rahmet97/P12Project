from django.urls import path
from .views import HomeView, about, product, Contact, remote, video, ProductDetail

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', about),
    path('product', product),
    path('remote', remote),
    path('video', video),
    path('contact', Contact.as_view(), name='contact'),
    path('product/<int:pk>', ProductDetail.as_view(), name='product_detail'),
]