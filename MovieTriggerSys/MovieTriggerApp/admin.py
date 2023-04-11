from django.contrib import admin
from . import models
from django.urls import reverse
from django.db.models import Count,Value
from django.utils.http import  urlencode
from django.utils.html import format_html
# Register your models here.




#  this is the inline children code its not working
# # we can write a trigger while creating a movie 
# # add a children inline 
# class TriggerInline(admin.StackedInline):
#     # overriding thew model i want to make it inline
#     model = models.Trigger
#     extra = 0


# MOVIE MODEL
@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    # form fields
    fields=[("title","description"),('age_rating','trigger','genre')]
    # search field so it can be searchable 
    search_fields=['title']
    
    # display fields 
    fields = ['trigger']
    list_display=['MID','title','description','age_rating','TopMovies', 'trigger','trigger_name']
    list_editable=['age_rating']
    list_per_page=20
    list_filter=['age_rating']
    #list_select_related=['trigger']
    # ordering = ['Top5']

    # to make the genre and the trigger searcheable in the form
    autocomplete_fields=['trigger','genre']


# this is the inline children code its not working
    # Refernce the inline class 
    # inlines = [TriggerInline,]



#   COMPUTED COLUMN
    @admin.display(ordering='TopMovies' ,description="Is it in the top movies ?",boolean=True)
    def TopMovies(self,Movie:models.Movie):
        if Movie.title == "Viridiana":
            return True
        if Movie.title == "Hot Rod":
            return True  
        return False
    #    OVEERINDING BASE QUERYSET
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(TopMovies=Value(True))
    
# RELATED CLOUMN
    @admin.display(ordering='trigger__name')
    def trigger_name(self,movie:models.Movie):
        return movie.trigger.name
    







# VIEWER MODEL
@admin.register(models.Viewer)
class ViewerAdmin(admin.ModelAdmin):
    # FORM FIELDS
    fields=[("email","password")]
    # display fields 
    list_display=['VID','email','password']
    list_per_page=10
    list_filter=['email']



#this is the inline children code its not working
# we can create a movie while creating a list
# add a children inline 
# class MovieInline(admin.StackedInline):
#     # overriding thew model i want to make it inline
#     model = models.Movie
#     extra = 0
#     # what is the name of the fk 
#     fk_name = model.trigger



# LIST MODEL
@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):
    # form fields
    fields=[("name","description"),('movie','viewer')]
    # display fields 
    list_display=['LID','name','description']
    list_per_page=10
    list_filter=['name']


    #  this is the inline children code its not working
    # refrence the inline 
    # inlines = [MovieInline,]


# TRIGGER MODEL
@admin.register(models.Trigger)
class TriggerAdmin(admin.ModelAdmin):
    # form fields
    fields=[("name","description")]
    # display fields 
    list_display=['name','description']
    list_per_page=10
    list_filter=['name']
    # search field so it can be used in the autocomplete field
    search_fields=['trigger']


# GENRE MODEL
@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    # form fields
    fields=[("genre")]
    # display fields 
    list_display=['id','genre']
    list_editable=['genre']
    list_per_page=10
    list_filter=['genre']
    # search field so it can be used in the autocomplete field
    search_fields=['genre']





# REVIEW MODEL
@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    # form fields
    fields=[("description"),('age_rating','movie','viewer')]
    # display fields 
    list_display=['RID','description','rating']
    list_per_page=10
    list_filter=['rating']

