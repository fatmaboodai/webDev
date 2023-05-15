from ast import List
from django.contrib import admin
from . import models
from django.utils.html import format_html 
from django.urls import reverse
from django.db.models import Count,Value
from django.utils.http import  urlencode
from django.shortcuts import redirect
from django.db.models import Q
from django import forms
from django.forms.widgets import CheckboxSelectMultiple

# SUPERUSER INFO
# Username : admin
# Password: project123

# Register your models here.


#  we can create a movie while creating a trigger 
#  add a children inline 
class TriggerAdminInline(admin.StackedInline):
    # overriding thew model i want to make it inline
    model = models.Movie
    extra = 0


# we can create a movie while creating a list
# add a children inline 
class MovieAdminInline(admin.StackedInline):
    # overriding thew model i want to make it inline
    model = models.List
    extra = 0




# CUSTOM FILTER
class RatingFilter(admin.SimpleListFilter):
    title = 'Age rating status'
    parameter_name = 'age_rating'

    def lookups(self, request, model_admin):
        return [
            ('G', 'safe'),
            ('PG13', 'unsafe')
        ]
    
    def queryset(self, request, queryset):
        if self.value() == 'G':
            return queryset.filter( age_rating = 'G')
        if self.value() == 'PG':
            return queryset.filter( age_rating = 'PG')
        if self.value() == 'R':
            return queryset.filter( age_rating = 'R')
        if self.value() == 'PG13':
            return queryset.filter( age_rating = 'PG13')
        


class MovieForm(forms.ModelForm):
    class Meta:
        model = models.Movie
        fields = ['title', 'description', 'age_rating', 'trigger', 'genre']
        widgets = {
            'trigger': forms.CheckboxSelectMultiple,
        }


class ListForm(forms.ModelForm):
    class Meta:
        model = models.List
        fields= ["name","description",'type','movie','viewer']
        widgets = {
            'movie': forms.CheckboxSelectMultiple,
        }

# MOVIE MODEL
@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    form = MovieForm
    # form fields
    fields=[("title","description"),('age_rating','trigger','genre')]
    # to make the genre and the trigger searcheable in the form
    autocomplete_fields=['genre']

    # action
    actions = ['clear_rating']
        # display fields 
    # fields = ['trigger']
    list_display=['id','title','description','age_rating','TopMovies','trigger_name','age_rating_status','review','genre',]
    list_editable=['age_rating']
    list_per_page=20

    # search field so it can be searchable 
    search_fields=['title','trigger__name','trigger','genre']

    # add filter to the page that sorts by age rating
    # custom filter ?
    # list_filter=['age_rating', RatingFilter]
    list_filter=[ RatingFilter]
    list_select_related=['genre']
    # ordering = ['Top5']

    list_filter=['age_rating']


    # refrence the inline 
    # inlines = [MovieAdminInline]


#   COMPUTED COLUMN
    @admin.display(ordering='TopMovies' ,description="Is it in the top movies ?",boolean=True)
    def TopMovies(self,Movie:models.Movie):
        if Movie.title == "Viridiana":
            return True
        if Movie.title == "Hot Rod":
            return True  
        return False
    
    # OVEERINDING BASE QUERYSET

    @admin.display(ordering = 'age_rating')
    def age_rating_status(self, movie:models.Movie):
        if movie.age_rating == 'G':
            return 'safe'
        return 'unsafe'
    

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(TopMovies=Value(True))
    
    
    # testing importing the review in movies
    def review(self,review:models.Review):
        return review.description
    
    
# RELATED CLOUMN
# # TRIGGER NAME IN MOVIE LINKS TO OTHER PAGE
#     @admin.display(ordering='trigger__name')
#     def trigger_name(self,movie:models.Movie):
#         x= ','.join([trigger.name for trigger in movie.trigger.all()])
#         return format_html('<a href= "http://127.0.0.1:8000/admin/MovieTriggerApp/trigger/?name={}"> {} </a>', x, x)
#         # return redirect('admin:MovieTriggerApp/admin/TriggerAdmin', movie.trigger.name)




# TRIGGER NAME IN MOVIE LINKS TO OTHER PAGE
    @admin.display(ordering='trigger__name')
    def trigger_name(self, movie: models.Movie):
        trigger_names = ','.join([trigger.name for trigger in movie.trigger.all()])
        link = reverse('admin:MovieTriggerApp_trigger_changelist')
        url = f'{link}?name={trigger_names}'
        return format_html('<a href="{}">{}</a>', url, trigger_names)
    




# CREATE CUSTOM ACTION
    @admin.action(description='Clear Rating')
    def clear_rating(self, request, queryset):
        string_update = queryset.update(age_rating = '')
        self.message_user(request,
                          f'{string_update} products has been updated successfully')




# VIEWER MODEL
@admin.register(models.Viewer)
class ViewerAdmin(admin.ModelAdmin):
    # FORM FIELDS
    fields=[("email","password", "user")]
    # fields=[("email","password", "user")]

    list_select_related = ["user"]
    search_fields = ["user__email__istartswith"]
    ordering = ["user__email"]

    # display fields 
    list_display=['id','email','password']
    list_per_page=10
    #list_filter=['email']
    list_filter=['id']


    @admin.display(ordering="user__email")
    def email(self, viewer):
        return viewer.user.email
    
    




# LIST MODEL
@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):
    form=ListForm
    # form fields
    fields=[("name","description",'type'),('movie','viewer')]
    # fields=[("name","description"),('viewer')]
    # display fields 
    list_display=['id','name','description','movies','type']
    list_per_page=10
    list_filter=['name']
    def movies(self, obj):
        return ', '.join([movie.title for movie in obj.movie.all()])


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
    search_fields=['name__icontains']
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
    fields=[("description"),('rating','movie','Viewer')]
    # display fields 
    list_display=['id','description','rating','Viewer','movie']
    list_per_page=10
    list_filter=['rating']

