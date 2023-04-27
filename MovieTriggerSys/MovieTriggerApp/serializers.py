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
        fields = ['id','title','description','age_rating','genre','trigger']

    # primarykey related fiel
    # not sure
    id = serializers.PrimaryKeyRelatedField(read_only=True)

    #Related field as string
    # trigger = serializers.StringRelatedField()
    # nested serlizer
    genre = GenreSerializer()


        

        
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


   
    # primarykey related fiel
    id = serializers.PrimaryKeyRelatedField(read_only=True)

    def create(self, validated_data):
        movie_id=self.context('movie_id')
        return Review.objects.create(movie_id=movie_id,**validated_data)


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
        fields = ['id','email','password']

    # primarykey related fiel
    id = serializers.PrimaryKeyRelatedField(read_only=True)







# List serlizer
class ListSerializer(serializers.ModelSerializer):

    class Meta:
        model = List
        # MOVIE , VIEWER ARE  RELATED FIELDS AS A PK
        fields = ['id','name','movie','viewer','NumOfMovies']


    # #Related field as string
    viewer = serializers.StringRelatedField()

    # # primarykey related fiel
    id = serializers.PrimaryKeyRelatedField(read_only=True)

    # hyperlink related field
    movie = serializers.HyperlinkedRelatedField(
        queryset= Movie.objects.all(),
        view_name='movie-detail'
          )
    


    # COMPUTED COLUMN SERLIZER 
    NumOfMovies = serializers.SerializerMethodField(method_name='get_NumOfMovies')
    def get_NumOfMovies(self,list:List):
        # not ORM
        movies=0
        if list.movie.id:
            movies+=1
        return movies
    


    




    

    



