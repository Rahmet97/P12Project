from django.contrib import admin
from .models import Product, Category, Comment

admin.site.register((Product, Category, Comment))