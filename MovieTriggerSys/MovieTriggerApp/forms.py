from django import forms
from .models import *

class CreateMovieForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['name','type', 'description','movie','viewer']
    movies = forms.ModelMultipleChoiceField(
        queryset=Movie.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )