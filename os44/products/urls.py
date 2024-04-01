from django.urls import path
from products.views import hello, welcome,landing, product_details, products_home
urlpatterns = [


    path('helloworld', hello, name='hellopage'),
    path('wlcm',welcome, name='welcomepage' ),
    path('land', landing, name='allproducts'),
    # specify part of the url --> variable and must be integer
    path('prd/<int:id>', product_details, name='prd.details'),
    path('home', products_home, name='products.home')

]