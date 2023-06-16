from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name=_('name'))

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    price = models.FloatField(verbose_name=_('price'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('category'))
    image = models.ImageField(upload_to='pics', verbose_name=_('image'))
    description = models.TextField(verbose_name=_('description'))
    date = models.DateTimeField(auto_now_add=True, verbose_name=_('date'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class Comment(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    phone = models.CharField(max_length=30, verbose_name=_('phone'))
    message = models.TextField(verbose_name=_('message'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')