from django.shortcuts import render
from recipe_maker.models import *
# Create your views here.

def rv_home(request):

    recipe=add_recipe.objects.all()
    return render(request, 'recipe_viewer/html/rv_viewer.html',{'recipe':recipe})


def searchbar(request):
    print("mai search u ")
    query = request.GET.get('query')
    print("yaha tk to chal rha hai ")
    crse= add_recipe.objects.filter(recipe_name__icontains=query)
    return render(request, 'recipe_viewer/html/search_destination.html',{'crse':crse})

def recipe_details(request, recipe_name):
    print("ha ha aha mai chl gya")
    dish =add_recipe.objects.filter(recipe_name__icontains=recipe_name)
    return render(request, 'recipe_viewer/html/recipie_detail.html', {'dish': dish})


