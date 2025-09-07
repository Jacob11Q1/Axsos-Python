from django import forms
from .models import TVShow
from django.utils import timezone

class TVShowForm(forms.ModelForm):
    class Meta:
        model = TVShow
        fields = ['title', 'network', 'release_date', 'description']
        widgets = {
            # Make release_date use HTML5 date input (browser calendar picker)
            'release_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'network': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if TVShow.objects.filter(title__iexact=title).exists():
            raise forms.ValidationError("A TV show with this title already exists.")
        return title

    def clean_release_date(self):
        release_date = self.cleaned_data.get('release_date')
        if release_date > timezone.now().date():
            raise forms.ValidationError("Release date must be in the past.")
        return release_date

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description and len(description) < 10:
            raise forms.ValidationError("Description must be at least 10 characters.")
        return description
