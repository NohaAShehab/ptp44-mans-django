from django.urls import path
from products.views import (hello, welcome,landing, product_details,
        products_home, product_profile, products_index, product_show)
urlpatterns = [


    path('helloworld', hello, name='hellopage'),
    path('wlcm',welcome, name='welcomepage' ),
    path('land', landing, name='allproducts'),
    # specify part of the url --> variable and must be integer
    path('prd/<int:id>', product_details, name='prd.details'),
    path('home', products_home, name='products.home'),
    path('old/<int:id>', product_profile, name='products.profile'),
    path('', products_index, name='products.index'),
    path('<int:id>', product_show, name='products.show')

]