from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Custom User model extends Django’s AbstractUser
# This allows us to add extra fields later if needed (like bio, profile pic, etc.)
class User(AbstractUser):
    email = models.EmailField(unique=True)  # Enforce unique email
    created_at = models.DateTimeField(auto_now_add=True)  # Track account creation time

# Book model
class Book(models.Model):
    title = models.CharField(max_length=255)  # Book title
    description = models.TextField(blank=True)  # Optional description
    
    # One-to-many relationship → One user uploads many books
    uploaded_by = models.ForeignKey(
        User, 
        related_name="books_uploaded",  # lets us call user.books_uploaded.all()
        on_delete=models.CASCADE
    )
    
    # Many-to-many relationship → Many users can like many books
    users_who_like = models.ManyToManyField(
        User, 
        related_name="liked_books"  # lets us call user.liked_books.all()
    )
    
    created_at = models.DateTimeField(auto_now_add=True)  # When book was added
    updated_at = models.DateTimeField(auto_now=True)  # Last updated

    def __str__(self):
        return self.title