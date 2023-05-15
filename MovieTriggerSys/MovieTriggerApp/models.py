from django.db import models
from django.forms import ValidationError
from django.core.validators import MinValueValidator,MaxValueValidator,MinLengthValidator,MaxLengthValidator
from uuid import uuid4
import uuid
from django.conf import settings


# Create your models here.
class Trigger(models.Model):
    name = models.CharField(max_length = 255,unique=True)
    #  blank is for the admin interface validation that the description is optional (form validation)
    description = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name
    
    class Meta:
        permissions = [
            ('edit_trigger', 'Can edit trigger')
    
        ]

class Movie(models.Model):
    RATED_G = 'G'
    RATED_PG = 'PG'
    RATED_PG13 = 'PG13'
    RATED_R = 'R'
    
    AGE_RATINGS = [
        (RATED_G, 'G'),
        (RATED_PG, 'PG'),
        (RATED_PG13, 'PG13'),
        (RATED_R, 'R')
    ]

    title = models.CharField(max_length = 255)
    #  blank is for the admin interface validation that the description is optional (form validation)
    description = models.TextField(blank=True,null=True)
    age_rating = models.CharField(max_length  = 4, choices = AGE_RATINGS, default = RATED_G)
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT)
    # a trigger is optional in a movie (form validation)
    trigger = models.ManyToManyField(Trigger,related_name='triggers')
    def __str__(self):
        return self.title
    class Meta:
        unique_together = ['genre','title']
    

class Genre(models.Model):
    ACTION = 'A'
    COMEDY = 'C'
    DRAMA = 'D'
    FANTASY = 'F'
    HORROR = 'H'
    MYSTERY = 'M'
    ROMANCE = 'R'

    GENRE_CHOICES = [
        (ACTION, 'Action'),
        (COMEDY, 'Comedy'),
        (DRAMA, 'Drama'),
        (FANTASY, 'Fantasy'),
        (HORROR, 'Horror'),
        (MYSTERY, 'Mystery'),
        (ROMANCE, 'Romance')
    ]
    genre = models.CharField(max_length = 255, choices = GENRE_CHOICES, default = DRAMA,unique = True)
    def __str__(self):
        return self.genre
    
class Viewer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # email = models.EmailField(unique = True)
    # Validators for the viewer's password
    password = models.CharField(max_length=255 , validators=[MinLengthValidator(8),MaxLengthValidator(20)])
    def __str__(self):
        return self.user.email
    
    class Meta:
        permissions = [
            ('view_users', 'Can view users')
        ]



class Review(models.Model):
    Viewer = models.ForeignKey(Viewer, on_delete=models.CASCADE)
    #  blank is for the admin interface validation that the description is optional (form validation)
    description = models.TextField(blank=True,null=True)
    # form validations for the ratings
    rating = models.IntegerField(validators = [MinValueValidator(1),MaxValueValidator(5)])
    #  to map the movie to thr movie model
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    class Meta:
        unique_together = ['Viewer','movie']
    


    

class List(models.Model):
    name = models.CharField(max_length = 255)
    #  blank is for the admin interface validation that the description is optional (form validation)
    WATCHLIST = 'WL'
    WATCHED = 'W'
    FAVORITES= 'F'
    BLOCKED = 'B'
    LIST_TYPES = [
        (WATCHLIST, 'Watch List'),
        (WATCHED, 'Watched'),
        (FAVORITES, 'Favorites'),
        (BLOCKED, 'Blocked'),
    ]
    type = models.CharField(max_length = 255, choices = LIST_TYPES, default = WATCHLIST)
    description = models.TextField(blank=True , null=True)
    movie = models.ManyToManyField(Movie,related_name='movie')
    viewer = models.ForeignKey(Viewer, on_delete=models.CASCADE)

    


# class Movie_list(models.Model):
#     movie =models.ForeignKey(Movie,on_delete=models.CASCADE)
#     list =models.ForeignKey(List,on_delete=models.CASCADE)
