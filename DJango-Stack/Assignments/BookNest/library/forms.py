from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Book

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        "class":"form-control", "placeholder":"Email"
    }))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # add bootstrap classes
        self.fields["username"].widget.attrs.update({"class":"form-control", "placeholder":"Username"})
        self.fields["password1"].widget.attrs.update({"class":"form-control", "placeholder":"Password"})
        self.fields["password2"].widget.attrs.update({"class":"form-control", "placeholder":"Confirm Password"})

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("title", "description")
        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control", "placeholder":"Title", "maxlength":"255"}),
            "description": forms.Textarea(attrs={"class":"form-control", "placeholder":"Short description", "rows":"4"}),
        }
