from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    # Multi-select authors field
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # You can change to SelectMultiple if preferred
        required=True,
        label="Authors"
    )

    class Meta:
        model = Book
        fields = ['title', 'description', 'authors']  # Explicit is better than __all__
        labels = {
            'title': 'Book Title',
            'description': 'Book Description',
        }
