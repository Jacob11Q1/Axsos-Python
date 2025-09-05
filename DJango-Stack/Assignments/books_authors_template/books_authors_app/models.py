from django.db import models

# Create your models here.

# Author Model Class:
class Author(models.Model):
    name = models.CharField(max_length = 255) # Author name
    created_at = models.DateTimeField(auto_now_add = True) # Auto timestamp
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name

# Book Model Class:
class Book(models.Model):
    title = models.CharField(max_length = 255) # Book title
    description = models.TextField() # Book description
    authors = models.ManyToManyField(Author, related_name = 'books') # Many-to-many relationship
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.title