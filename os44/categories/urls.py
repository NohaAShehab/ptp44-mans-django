
from categories.views import landing
from django.urls import path

# include categories urls
urlpatterns = [

path('cats', landing, name='categories')

]