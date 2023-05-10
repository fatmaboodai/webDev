from rest_framework import serializers
from .models import *
from django.db.models import Count,Value
from decimal import Decimal


# genre serlizer
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre']


# Movie serlizer
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # genre , trigger ARE  RELATED FIELDS AS A PK
        fields = ['title','description','age_rating','genre','trigger']

    #Related field as string
    # trigger = serializers.StringRelatedField()
    # nested serlizer
    genre = GenreSerializer()


class UpdateMovie(serializers.ModelSerializer):
    class Meta:
        model = Movie
        field = ['title', 'description','age_rating','trigger_id','genre']

class CreateMovie(serializers.ModelSerializer):
    def save(self, **kwargs):
        title = self.validated_data['title']
        description = self.validated_data['description']
        age_rating = self.validated_data['age_rating']
        trigger_id = self.validated_data['trigger']
        genre_id = self.context['genre']
        # movie_id = self.context['movie_id']
        try:
            #updating existing record
            movie = Movie.objects.get(genre_id=genre_id,trigger_id=trigger_id)
            movie.title = title
            movie.description = description
            movie.age_rating = age_rating
            movie.trigger = trigger_id
            movie.genre = genre_id
            movie.save()
            self.instance = movie
            
        except Movie.DoesNotExist:
            #creating a new record
            self.instance = Movie.objects.create(genre_id=genre_id,**self.validated_data)
        return self.instance
    
    class Meta:
        model = Movie
        fields = ['title', 'description','age_rating','trigger','genre']



        
# custom serlizer
class SimpleMovieSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields=['title','genre','trigger']
    genre = serializers.StringRelatedField()
    trigger = serializers.StringRelatedField()
    

# Reviw serlizer
class ReviewSerializer(serializers.ModelSerializer):
    movie = SimpleMovieSerlizer()
    class Meta:
        model = Review
        # MOVIE , VIEWER ARE  RELATED FIELDS AS A PK
        fields = ['id','Viewer','description','rating','movie']


    # string related field
    Viewer = serializers.StringRelatedField()


    def create(self, validated_data):
        movie_id=self.context['movie_id']
        return Review.objects.create(movie_id=movie_id,**validated_data)
    
class UpdateReview(serializers.ModelSerializer):
    class Meta:
        model = Movie
        field = ['description','rating']

class CreateReview(serializers.ModelSerializer):
    def save(self, **kwargs):
        Viewer_id = self.validated_data['Viewer']
        description = self.validated_data['description']
        rating = self.validated_data['rating']
        movie_id = self.context['movie_id']
        try:
            #updating existing record
            review = Review.objects.get(movie_id=movie_id,Viewer_id=Viewer_id)
            review.description = description
            review.rating = rating
            review.save()
            self.instance = review
        except Review.DoesNotExist:
            #creating a new record
            self.instance = Review.objects.create(movie_id=movie_id,**self.validated_data)
        return self.instance
    
    class Meta:
        model = Review
        fields = ['Viewer', 'description','rating','movie']



# Trigger serlizer
class TriggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trigger
        fields = ['id','name','description']


# Viewer serlizer
class ViewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viewer
        fields = ['id','email','password']


# List serlizer
class ListSerializer(serializers.ModelSerializer):
    # movie =Movie.objects.all()
    class Meta:
        model = List
        # MOVIE , VIEWER ARE  RELATED FIELDS AS A PK
        fields = ['name','movie','viewer','NumOfMovies']
        # fields = ['name','movie','viewer']


    # #Related field as string
    viewer = serializers.StringRelatedField()

    # hyperlink related field
    movie = serializers.HyperlinkedRelatedField(
        queryset= Movie.objects.all(),
        view_name='movie-detail',
        many=True,
         )
    # COMPUTED COLUMN SERLIZER 
    NumOfMovies = serializers.SerializerMethodField(method_name='get_NumOfMovies',read_only=True)
    def get_NumOfMovies(self,list:List):
        # # not ORM
        # movies=0
        # if list.movie.id:
        #     movies+=1
        return list.movie.count()
    
    def create(self, validated_data):
        viewer_id = self.context['viewer_id']
        return List.objects.create(viewer_id = viewer_id, **validated_data)
   
    


    



    

    



