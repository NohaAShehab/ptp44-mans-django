from django.urls import path
from django.contrib.auth.decorators import  login_required
from products.views import (hello, welcome,landing, product_details,
        products_home, product_profile, products_index, product_show,
                            product_delete, product_create, product_create_forms,
                            create_product_model_form, edit_product)
urlpatterns = [


    path('helloworld', hello, name='hellopage'),
    path('wlcm',welcome, name='welcomepage' ),
    path('land', landing, name='allproducts'),
    # specify part of the url --> variable and must be integer
    path('prd/<int:id>', product_details, name='prd.details'),
    path('home', products_home, name='products.home'),
    path('old/<int:id>', product_profile, name='products.profile'),
    path('', products_index, name='products.index'),
    path('<int:id>', product_show, name='products.show'),
    path('<int:id>/delete', product_delete, name='products.delete'),
    path('create', product_create, name='products.create'),
    path('forms/create', product_create_forms, name='products.create.forms'),
    path('forms/createmodel', create_product_model_form, name='product.createmodel'),
    path('forms/<int:id>/edit',login_required(edit_product), name='products.edit' )

]