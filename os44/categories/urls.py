
from categories.views import landing
from django.urls import path
from categories.views import home
# include categories urls
urlpatterns = [

    path('cats', landing, name='categories'),
    path('home',home, name='categories.home' )

]