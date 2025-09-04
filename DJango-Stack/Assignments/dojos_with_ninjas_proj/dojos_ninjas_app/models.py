from django.db import models

# Create your models here.

# Dojo Class Model:
class Dojo(models.Model):
    name = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 2)
    
    def __str__(self):
        return f"{self.name} ({self.city}, {self.state})"

# Ninja Class Model - One to Many Relationship:
class Ninja(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    dojo = models.ForeignKey(
        Dojo, 
        related_name = "ninjas",
        on_delete = models.CASCADE
        )
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"