from django.db import models
from django.forms import ValidationError

from django.core.validators import MinValueValidator,MaxValueValidator,MinLengthValidator,MaxLengthValidator


# Create your models here.


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

    MID = models.CharField(max_length = 255, primary_key=True)
    title = models.CharField(max_length = 255)
    #  blank is for the admin interface validation that the description is optional (form validation)
    description = models.TextField(blank=True)
    age_rating = models.CharField(max_length  = 4, choices = AGE_RATINGS, default = RATED_G)
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT)
    # a trigger is optional in a movie (form validation)
    trigger = models.ForeignKey('Trigger', on_delete=models.PROTECT,blank=True)
    def __str__(self):
        return self.title



class Trigger(models.Model):
    name = models.CharField(max_length = 255)
    #  blank is for the admin interface validation that the description is optional (form validation)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

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
    genre = models.CharField(max_length = 255, choices = GENRE_CHOICES, default = DRAMA)
    def __str__(self):
        return self.genre
    

class Review(models.Model):
    RID = models.CharField(max_length = 255, primary_key=True)
    Viewer = models.ForeignKey('Viewer', on_delete=models.PROTECT)
    #  blank is for the admin interface validation that the description is optional (form validation)
    description = models.TextField(blank=True)
    # form validations for the ratings
    rating = models.IntegerField(validators = [MinValueValidator(1),MaxValueValidator(5)])
    #  to map the movie to thr movie model
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    



class Viewer(models.Model):
    VID = models.CharField(max_length = 255, primary_key=True)
    email = models.EmailField(unique = True)
    # Validators for the viewer's password
    password = models.CharField(max_length=255 , validators=[MinLengthValidator(8),MaxLengthValidator(20)])
    def __str__(self):
        return self.email

class List(models.Model):
    LID = models.CharField(max_length = 255, primary_key=True)
    name = models.CharField(max_length = 255)
     #  blank is for the admin interface validation that the description is optional (form validation)
    description = models.TextField(blank=True)
    movie = models.ForeignKey('Movie', on_delete=models.PROTECT)
    viewer = models.ForeignKey('Viewer', on_delete=models.PROTECT)
