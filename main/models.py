from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.ImageField(upload_to='pics')
    description = models.TextField()

    def __str__(self):
        return self.title
