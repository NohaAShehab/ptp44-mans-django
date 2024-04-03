##django imports
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from products.forms import  ProductForm, ProductModelForm

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


def product_delete(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    # return HttpResponse("Product deleted")
    url = reverse("products.index")
    return redirect(url)


def product_create(request):
    print(request)
    if request.method == "POST":
        print(request.FILES)
        if request.FILES:
            image = request.FILES["image"]
        else:
            image = None
        print(request.POST)
        product = Product(name=request.POST["name"], price=request.POST["price"],
                          code=request.POST["code"], image=image)
        product.save()
        return redirect(product.show_url)
        # return HttpResponse("Post request received")
    # post request

    # get request
    return  render(request, 'products/crud/create.html')



def product_create_forms(request):
    # use form class
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)

            product = Product(name=form.cleaned_data['name'], price=form.cleaned_data['price'],
                              image=form.cleaned_data['image'], code=form.cleaned_data['code'])
            product.save()
            return redirect(product.show_url)

    return render(request, 'products/forms/create.html',
                  context={'form':form})



def create_product_model_form(request):
    form = ProductModelForm()
    if request.method == "POST":
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            product=form.save()
            return redirect(product.show_url)

    return render(request, 'products/forms/createmodelform.html',
                  context={"form": form})







