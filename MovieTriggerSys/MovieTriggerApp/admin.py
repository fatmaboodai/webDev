from django.contrib import admin
from . import models
from django.urls import reverse
from django.db.models import Count,Value
from django.utils.http import  urlencode
from django.utils.html import format_html
# Register your models here.



@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    # display fields 
    # fields=[("description","")]
    list_display=['MID','title','description','age_rating','TopMovies',"trigger__name"]
    list_editable=['age_rating']
    list_per_page=20
    list_filter=['age_rating']
    list_select_related=['trigger']
    # ordering = ['Top5']

    @admin.display(ordering='TopMovies' ,description="Is it in the top movies ?",boolean=True)
    def TopMovies(self,Movie:models.Movie):
        if Movie.title == "Viridiana":
            return True
        if Movie.title == "Hot Rod":
            return True  
        return False
       
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(TopMovies=Value(True))
    

    @admin.display(ordering='trigger__name')
    def trigger__name(self,movie:models.Movie):
        return movie.trigger.name




@admin.register(models.Viewer)
class ViewerAdmin(admin.ModelAdmin):
    # display fields 
    list_display=['VID','email','password']
    list_per_page=10
    list_filter=['email']


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):
    # display fields 
    list_display=['LID','name','description']
    list_per_page=10
    list_filter=['name']



@admin.register(models.Trigger)
class TriggerAdmin(admin.ModelAdmin):
    # display fields 
    list_display=['name','description']
    list_per_page=10
    list_filter=['name']


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    # display fields 
    list_display=['id','genre']
    list_editable=['genre']
    list_per_page=10
    list_filter=['genre']



@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    # display fields 
    list_display=['RID','description','rating']
    list_per_page=10
    list_filter=['rating']

