"""
URL configuration for os44 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from products.views import hello, welcome, landing, product_details
from categories.views import  landing as cat_landing
urlpatterns = [
    path('admin/', admin.site.urls),
    # path(url, viewname, name='anyname')
    # path('helloworld', hello, name='hellopage'),
    # path('wlcm',welcome, name='welcomepage' ),
    # path('land', landing, name='allproducts'),
    # # specify part of the url --> variable and must be integer
    # path('prd/<int:id>', product_details, name='prd.details'),
    # path('cats', cat_landing, name='categories')


    # include categories urls file in main url
    path('categories/', include('categories.urls')),

    ##include products urls
    path('products/', include("products.urls"))
]


