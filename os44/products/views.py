##django imports
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

## python imports
import json


## imports from your created files
from products.models import Product

# Create your views here.

##function views

def hello(request): ## accept http request
    """ return with http response """
    print(request)
    return HttpResponse("We are here")


def welcome(request):
    name = "Ahmed"
    return HttpResponse(f"<h1 style='color:red'>Welcome{name} </h1>")




products = [
    {"id":1 , 'name':"iphone","price": 80000, "image": "pic1.png"},
    {"id":2 , 'name':"Kia sportage","price": 1000000, "image": "pic22.png"},
    {"id":3 , 'name':"MACBOOK","price": 100000, "image": "pic33.png"},
    {"id":4 , 'name':"airpods","price": 30000, "image": "pic44.png"},

]

def landing(request):
    return HttpResponse(products)


def product_details(request,id):
    print(type(id))
    id = int(id)
    filtered_products = filter(lambda product: product['id'] == id, products) # filter object
    print(filtered_products)
    allproducts = list(filtered_products)
    print(allproducts)
    if allproducts:
        # return HttpResponse(allproducts[0].values())
        return HttpResponse(json.dumps(allproducts[0]))
    return  HttpResponse("No product found ")



def products_home(request):
    # return with template home.html
    return render(request, "products/home.html",
                  context = {"name": "noha", "products": products},
                  status=200)  # render http response



def product_profile(request, id):
    filtered_products = filter(lambda product: product['id'] == id, products)
    filtered_products = list(filtered_products)
    if filtered_products:
        product = filtered_products[0]
        return render(request, "products/details.html", context={
            "product": product
        })

    return HttpResponse("product not found")






def products_index(request):
    products  = Product.objects.all()
    return render(request, "products/crud/index.html",
                  context={"products": products})


def product_show(request, id):
    # product = Product.objects.get(id=id)
    product = get_object_or_404(Product, pk=id)
    return render(request, "products/crud/show.html", context={"product": product})