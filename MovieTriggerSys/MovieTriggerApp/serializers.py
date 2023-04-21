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
        fields = ['MID','title','description','age_rating','genre','trigger']

    # primarykey related fiel
    # not sure
    MID = serializers.PrimaryKeyRelatedField(read_only=True)

    #Related field as string
    trigger = serializers.StringRelatedField()
    # nested serlizer
    genre = GenreSerializer()

    # hyperlink related field
    # trigger = serializers.HyperlinkedRelatedField(
    #     queryset= Trigger.objects.all(),
    #     view_name='trigger-details'
    #       )

        
# Reviw serlizer
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        # MOVIE , VIEWER ARE  RELATED FIELDS AS A PK
        fields = ['RID','Viewer','description','rating','movie']

    
    #Related field as string
    movie = serializers.StringRelatedField()
    Viewer = serializers.StringRelatedField()

    # primarykey related fiel
    RID = serializers.PrimaryKeyRelatedField(read_only=True)

    def create(self, validated_data):
        # movie_id=self.context('movie_id')
        viewer_id = self.context('Viewer_id')
        return Review.objects.create(viewer_id=viewer_id,**validated_data)

        # return Review.objects.create(movie_id=movie_id,**validated_data)


# Trigger serlizer
class TriggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trigger
        fields = ['id','name','description']
    # primarykey related fiel
    # not sure
    id = serializers.PrimaryKeyRelatedField(read_only=True)




# Viewer serlizer
class ViewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viewer
        fields = ['VID','email','password']

    # primarykey related fiel
    VID = serializers.PrimaryKeyRelatedField(read_only=True)




# custom serlizer
class SimpleMovieSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields=['title','genre','trigger']
    genre = serializers.StringRelatedField()
    trigger = serializers.StringRelatedField()
    




# List serlizer
class ListSerializer(serializers.ModelSerializer):
    movie = SimpleMovieSerlizer()
    class Meta:
        model = List
        # MOVIE , VIEWER ARE  RELATED FIELDS AS A PK
        fields = ['LID','name','movie','viewer','NumOfMovies']


    # #Related field as string
    # movie = serializers.StringRelatedField()
    viewer = serializers.StringRelatedField()

    # # primarykey related fiel
    LID = serializers.PrimaryKeyRelatedField(read_only=True)
    

    # COMPUTED COLUMN SERLIZER 
    NumOfMovies = serializers.SerializerMethodField(method_name='get_NumOfMovies')
    def get_NumOfMovies(self,list:List):
        # not ORM
        movies = list.movie.MID
        return len(movies)
    

    



