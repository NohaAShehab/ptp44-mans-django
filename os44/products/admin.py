from django.contrib import admin

# Register your models here.
from products.models import Product

admin.site.register(Product)

## you can customize operations you need to appear in the admin dashboard