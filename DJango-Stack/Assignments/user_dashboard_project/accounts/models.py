"""Models for accounts app. We'll use Django's built-in User model for auth
    and create a Profile to store extra user data (like avatar)."""

from django.db import models  # Django ORM models
from django.contrib.auth.models import User  # built-in User model
from django.db.models.signals import post_save  # signal to create profile on user creation
from django.dispatch import receiver  # decorator to register signal receiver

# Create your models here.

class Profile(models.Model):
    """Profile model that extends built-in User with an avatar and bio."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # link profile to a user
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)  # avatar image (optional)
    bio = models.TextField(blank=True, default="")  # short bio text

    def __str__(self):
        """String representation of profile for admin or debugging."""
        return f"{self.user.username} Profile"

# create / save profile automatically when a user is created
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver: when a User is saved, make sure a Profile exists.
    If created: create a new Profile.
    Otherwise: save the existing profile.
    """
    if created:
        Profile.objects.create(user=instance)  # create profile for new user
    else:
        try:
            instance.profile.save()  # save profile for existing user
        except Exception:
            # in rare case profile doesn't exist, create it
            Profile.objects.get_or_create(user=instance)
