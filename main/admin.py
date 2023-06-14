from django.contrib import admin
from .models import Product, Category, Comment
from modeltranslation.admin import TranslationAdmin


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    pass


admin.site.register((Category, Comment))
