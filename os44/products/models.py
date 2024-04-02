from django.db import models

# Create your models here.

class Product(models.Model):
    ## define columns  ---> datatypes
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    code = models.CharField(max_length=100 , unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


