from django_filters.rest_framework import FilterSet
from .models import *
# custom filter
class MovieFilter(FilterSet):
    class Meta:
        model = Movie
        fields = {
            'genre_id':['exact'],
            'age_rating':['exact']
        }