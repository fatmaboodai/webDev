from django.db import models
from django.forms import ValidationError
from django.core.validators import MinValueValidator,MaxValueValidator


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
    description = models.TextField()
    age_rating = models.CharField(max_length  = 4, choices = AGE_RATINGS, default = RATED_G)
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT,null=True)
    trigger = models.ForeignKey('Trigger', on_delete=models.PROTECT,null=True)
    review = models.ForeignKey('Review', on_delete=models.PROTECT,null=True)



class Trigger(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()

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

class Review(models.Model):
    RID = models.CharField(max_length = 255, primary_key=True)
    Viewer = models.ForeignKey('Viewer', on_delete=models.PROTECT,null=True)
    description = models.TextField(null=True)
    rating = models.IntegerField(validators = (MinValueValidator(1),MaxValueValidator(5)),null=True)



class Viewer(models.Model):
    VID = models.CharField(max_length = 255, primary_key=True)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length=255)

class List(models.Model):
    LID = models.CharField(max_length = 255, primary_key=True)
    name = models.CharField(max_length = 255)
    description = models.TextField()
    movie = models.ForeignKey('Movie', on_delete=models.PROTECT,null=True)
    viewer = models.ForeignKey('Viewer', on_delete=models.PROTECT,null=True)
