from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True) # when the user is created
    updated_at = models.DateTimeField(auto_now=True) # when the user is updated
    
    def __str__(self):
        return f"User: {self.first_name} {self.last_name}"