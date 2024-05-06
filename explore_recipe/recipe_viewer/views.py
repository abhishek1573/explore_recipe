from django.shortcuts import render
from recipe_maker.models import *
# Create your views here.

def rv_home(request):

    recipe=add_recipe.objects.all()
    return render(request, 'recipe_viewer/html/rv_home.html',{'recipe':recipe})


def search(request):
    query = request.GET.get('query')
    crse= add_recipe.objects.filter(recipe_name__icontains=query)
    return render(request, 'recipe_viewer/html/search_destination.html',{'crse':crse})

