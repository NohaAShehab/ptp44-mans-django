from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from categories.forms import CategoryModelForm
from categories.models import  Category

# Create your views here.


def landing(request):
    return HttpResponse("<h1>Welcome to Categories app </h1>")

def home(request):
    return render(request, "categories/home.html")


def create_category(request):
    form = CategoryModelForm()
    if request.method == "POST":
        form = CategoryModelForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save()
            url =  reverse("categories.index")
            return  redirect(url)



    return render(request, 'categories/create.html',
                  {'form': form})





def categories_index(request):
    categories = Category.get_all_categories()
    return render(request, 'categories/index.html', {'categories' : categories})



def category_show(request, id):
    category = Category.get_category_by_id(id)
    return render(request, 'categories/show.html', {'category' : category})