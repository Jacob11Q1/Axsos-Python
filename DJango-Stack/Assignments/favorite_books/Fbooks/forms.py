from django import forms
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from .models import User

# Book Form
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Book title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'rows': 4}),
        }

# Registration Form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
