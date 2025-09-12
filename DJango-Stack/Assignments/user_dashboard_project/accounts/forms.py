"""Forms for registration and login using Django forms + crispy for bootstrap styling."""

from django import forms  # Django forms framework
from django.contrib.auth.models import User  # built-in User model
from django.contrib.auth.forms import AuthenticationForm  # default login form
from django.core.exceptions import ValidationError  # for custom validation

class RegisterForm(forms.ModelForm):
    """
    Simple registration form that inherits from ModelForm for the User model.
    We explicitly add password fields and validate them match.
    """
    password = forms.CharField(widget=forms.PasswordInput, label="Password")  # password input
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm password")  # confirm password

    class Meta:
        model = User  # use the User model
        fields = ["username", "email"]  # fields to display in the form

    def clean_password2(self):
        """Ensure the two typed passwords match."""
        p1 = self.cleaned_data.get("password")
        p2 = self.cleaned_data.get("password2")
        if p1 and p2 and p1 != p2:
            # raise validation error if passwords don't match
            raise ValidationError("Passwords do not match")
        return p2

    def save(self, commit=True):
        """Create the user with hashed password."""
        user = super().save(commit=False)  # get unsaved user instance
        user.set_password(self.cleaned_data["password"])  # hash password
        if commit:
            user.save()  # save user to DB
        return user

class CustomLoginForm(AuthenticationForm):
    """Custom login form (keeps defaults but allows future customization)."""
    # using AuthenticationForm keeps username/password checking and messages
    pass
