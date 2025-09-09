from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# ----------------------------
# Custom User model
# ----------------------------
class User(AbstractUser):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Fix for groups & permissions conflict
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='fbooks_user',  # unique related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='fbooks_user_permissions',  # unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

# ----------------------------
# Book model
# ----------------------------
class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    uploaded_by = models.ForeignKey(
        User, related_name="books_uploaded", on_delete=models.CASCADE
    )
    users_who_like = models.ManyToManyField(
        User, related_name="liked_books", blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def likes_count(self):
        return self.users_who_like.count()
