from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.rv_home,name="rv_home"),
    path('search/', views.search,name="search"),
]
