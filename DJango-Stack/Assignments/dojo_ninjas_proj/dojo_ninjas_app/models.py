from django.db import models

# Create your models here.

# Dojo Model Class
class Dojo(models.Model):
    name = models.CharField(max_length = 255) # name of dojo
    city = models.CharField(max_length = 255) # city where is dojo located
    state = models.CharField(max_length = 2) # state obbreviation (2 chars)
    desc = models.TextField(default = "old dojo") 
    
    def __str__(self):
        return self.name # to show dojo name when printing it

# Ninja Model Class
class Ninja(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    dojo = models.ForeignKey(
        Dojo, # refers to the class Dojo Model
        related_name = "ninjas", # to allow the dojo.ninjas.all() to get all things fron ninjas
        on_delete = models.CASCADE # Delete Ninjas if dojo is deleted
    )
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}" # Printing the full name