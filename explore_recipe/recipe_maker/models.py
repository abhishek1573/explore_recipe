from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



# username explore123
# password explore123

class add_recipe(models.Model):
    first_name = models.CharField(null=True, blank=True,max_length=40)
    last_name = models.CharField(null=True, blank=True, max_length=40)
    recipe_name = models.CharField(null=True, blank=True, max_length=40)
    recipe_desc = models.CharField(null=True, blank=True, max_length=400)
    recipe_ingridient = models.CharField(null=True, blank=True, max_length=400)
    dish_image = models.ImageField(upload_to='recipe_maker/images/',null=True, blank=True,)
    recipe_instructions = models.CharField(null=True, blank=True, max_length=4000)
    Location = models.CharField(null=True, blank=True,max_length=50)
    Email_id = models.CharField(null=True, blank=True,max_length=50)


    def __str__(self):
        return self.recipe_name or "No Name"


