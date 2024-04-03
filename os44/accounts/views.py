from django.shortcuts import render, redirect, reverse
# Create your views here.


def profile_view(request):
    url= reverse("products.index")
    return redirect(url)