from django.db import models
from django.shortcuts import  reverse

# Create your models here.

class Product(models.Model):
    ## define columns  ---> datatypes
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    code = models.CharField(max_length=100 , unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.name}'

    @property
    def show_url(self):
        pass
        url = reverse('products.show', args=[self.id])
        return url
