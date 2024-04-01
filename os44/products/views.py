from django.shortcuts import render
from django.http import HttpResponse
import json
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
    {"id":2 , 'name':"Kia sportage","price": 1000000, "image": "pic2.png"},
    {"id":3 , 'name':"MACBOOK","price": 100000, "image": "pic3.png"},
    {"id":2 , 'name':"airpods","price": 30000, "image": "pic4.png"},

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
    return render(request, "products/home.html", status=200)  # render http response








