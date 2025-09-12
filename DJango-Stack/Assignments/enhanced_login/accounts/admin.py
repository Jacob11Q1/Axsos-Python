from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.utils.html import format_html
from .models import User

# ---------------- Custom Forms ----------------
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'birthday', 'profile_image')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'birthday', 'profile_image', 
                    'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')

# ---------------- Fancy Admin ----------------
class UserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ('profile_image_display', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'birthday', 'profile_image', 'profile_preview')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'created_at')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'birthday', 'profile_image', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )

    def profile_image_display(self, obj):
        if obj.profile_image:
            return format_html(
                '<div style="display:flex;align-items:center;"><img src="{}" width="50" height="50" style="border-radius:50%;margin-right:10px"/>'
                '<span>{}</span></div>', obj.profile_image.url, obj.email)
        return "(No image)"
    profile_image_display.short_description = "Profile"

    def profile_preview(self, obj):
        if obj.profile_image:
            return format_html('<img src="{}" width="150" height="150" style="border-radius:50%;border:2px solid #555"/>', obj.profile_image.url)
        return "(No profile image)"
    profile_preview.short_description = "Profile Preview"

# ---------------- Register the admin ----------------
admin.site.register(User, UserAdmin)
