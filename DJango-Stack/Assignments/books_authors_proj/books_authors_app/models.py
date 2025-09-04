from django.db import models

# Create your models here.

# Class Book Model:
class Book(models.Model):
    name = models.CharField(max_length = 255)
    desription = models.TextField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name

# Class Author Model:
class Author(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    notes = models.TextField(null = True, blank = True)
    books = models.ManyToManyField(Book, related_name = "authors")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"