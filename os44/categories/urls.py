
from categories.views import landing
from django.urls import path
from categories.views import home, create_category, categories_index, category_show
# include categories urls
urlpatterns = [

    path('cats', landing, name='categories'),
    path('home',home, name='categories.home' ),
    path('create', create_category, name='categories.create'),
    path('', categories_index, name='categories.index'),
    path('<int:id>', category_show, name='categories.show')



]