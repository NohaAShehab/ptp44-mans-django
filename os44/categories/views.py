from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def landing(request):
    return HttpResponse("<h1>Welcome to Categories app </h1>")

def home(request):
    return render(request, "categories/home.html")