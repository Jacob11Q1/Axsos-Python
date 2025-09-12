from django.contrib import admin
from .models import Profile

# Register your models here.

# Register Profile model so it appears in Django admin
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "bio")  # columns to display in admin list