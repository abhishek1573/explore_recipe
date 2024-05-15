from django.shortcuts import render
from . models import *

# Create your views here.

def rm_home(request):

    recipe=add_recipe.objects.all()
    print(recipe)
    return render(request, 'recipe_maker/html/rm_home.html',{'recipe':recipe})


def rm_add(request):
    return render(request, 'recipe_maker/html/rm_add_recipe.html')


def rm_adding_recipe(request):

    rm_firstname = request.POST.get('fname')
    rm_lastname = request.POST.get('lname')
    rm_recipename = request.POST.get('rname')
    rm_recipedesc = request.POST.get('rdesc')
    rm_ingridient = request.POST.get('ing')
    rm_dishphoto = request.POST.get('dishimg')
    rm_instruction = request.POST.get('instruction')
    rm_location = request.POST.get('place')
    rm_emailid = request.POST.get('emailid')

    if (rm_recipename != None):

            print(rm_recipename,rm_lastname,rm_emailid,rm_ingridient)
            sql = add_recipe(first_name=rm_firstname, last_name=rm_lastname, recipe_name=rm_recipename,recipe_desc=rm_recipedesc,recipe_ingridient=rm_ingridient, dish_image=rm_dishphoto,recipe_instructions=rm_instruction, Location=rm_location, Email_id=rm_emailid)
            sql.save()
            recipe = add_recipe.objects.all()
            return render(request, 'recipe_maker/html/rm_home.html', {'recipe': recipe})




    else:
        print("not working")
        return render(request, 'recipe_maker/html/rm_add_recipe.html')





