from django.urls import path , include
from . import views
from django.contrib import admin
from django.urls import path , include
from django.contrib import admin






urlpatterns = [
    path('', views.rv_home,name="rv_home"),
    path('search/', views.searchbar,name="search"),
    path('recipe_viewer/<str:recipe_name>/', views.recipe_details, name='recipe_details'),
]
