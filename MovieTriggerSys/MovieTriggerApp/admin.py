from django.contrib import admin
from . import models
from django.utils.html import format_html
from django.urls import reverse
from django.db.models import Count,Value
from django.utils.http import  urlencode
from django.utils.html import format_html
# Register your models here.




#  this is the inline children code its not working
# # we can write a trigger while creating a movie 
# # add a children inline 
class TriggerAdminInline(admin.StackedInline):
    # overriding thew model i want to make it inline
    model = models.Movie
    extra = 0

#this is the inline children code its not working
# we can create a movie while creating a list
# add a children inline 
class MovieAdminInline(admin.StackedInline):
    # overriding thew model i want to make it inline
    model = models.List
    extra = 0
    # what is the name of the fk 
    # fk_name = model.trigger

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
    
# MOVIE MODEL
@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    # form fields
    fields=[("title","description"),('age_rating','trigger','genre')]
    # action
    actions = ['clear_rating']
    # search field so it can be searchable 
    search_fields=['title']
    # display fields 
    fields = ['trigger']
    list_display=['MID','title','description','age_rating','TopMovies','trigger_name', 'age_rating_status']
    list_editable=['age_rating']
    list_per_page=20
    # add filter to the page that sorts by age rating
    list_filter=['age_rating', RatingFilter]
    #list_select_related=['trigger']
    # ordering = ['Top5']

    # to make the genre and the trigger searcheable in the form
    autocomplete_fields=['trigger','genre']
    #  this is the inline children code its not working
    # refrence the inline 
    inlines = [MovieAdminInline]

#   COMPUTED COLUMN
    @admin.display(ordering='TopMovies' ,description="Is it in the top movies ?",boolean=True)
    def TopMovies(self,Movie:models.Movie):
        if Movie.title == "Viridiana":
            return True
        if Movie.title == "Hot Rod":
            return True  
        return False
    #    OVEERINDING BASE QUERYSET

       
    @admin.display(ordering = 'age_rating')
    def age_rating_status(self, movie:models.Movie):
        if movie.age_rating == 'G':
            return 'safe'
        return 'unsafe'
    

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(TopMovies=Value(True))
    
# RELATED CLOUMN
# TRIGGER NAME IN MOVIE LINKS TO OTHER PAGE
    @admin.display(ordering='trigger__name')
    def trigger_name(self,movie:models.Movie):
        return format_html('<a href= "http://www.google.com"> {} </a>', movie.trigger.name)

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
    fields=[("email","password")]
    # display fields 
    list_display=['VID','email','password']
    list_per_page=10
    list_filter=['email']







# LIST MODEL
@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):
    # form fields
    fields=[("name","description"),('movie','viewer')]
    # display fields 
    list_display=['LID','name','description']
    list_per_page=10
    list_filter=['name']

    



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

    # this is the inline children code its not working
    # Refernce the inline class 
    inlines = [TriggerAdminInline]


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

