from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']
        labels = {
            'name': 'Author Name',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }
