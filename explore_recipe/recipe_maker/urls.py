from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('rm_home/', views.rm_home,name="rm_home"),
    path('rm_add/', views.rm_add,name="rm_add"),
    path('rm_adding_recipe/', views.rm_adding_recipe,name="adding_recipe"),

]
