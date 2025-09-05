from django.db import models

# Create your models here.

# Author Model Class:
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

# Book Model Class:
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    publish_date = models.DateField()
    authors = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return self.title