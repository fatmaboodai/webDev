from django_filters.rest_framework import FilterSet
from .models import *
# custom filter
class ReviewFilter(FilterSet):
    class Meta:
        model = Review
        fields = {
            'rating':['gt','lt']
        }