from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .models import *
from .serializers import * 
from rest_framework import status 
from rest_framework.viewsets import ModelViewSet
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,DestroyModelMixin
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ReviewFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import DefaultPagination

# Create your views here.


def ViewPage(request):
    # queryset = Movie.objects.all()
    queryset = Movie.objects.select_related('genre').all()
    list(queryset)
    return render(request,'MovieTriggerApp/index.html',{'name':'This is our Movie list','queryset':queryset})

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all().select_related('genre')
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title']
    filterset_fields= ['genre']
    ordering_fields = ['age_rating']
    pagination_class = DefaultPagination


    @action(detail=False, methods=['POST'])
    def AddMovie(self, request, *args, **kwargs):
        serializer = UpdateMovie(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        if self.request.method=='POST':
            return UpdateMovie
        if self.request.method=='PUT':
            return UpdateMovie
        return MovieSerializer

    
class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all().select_related('movie')
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['id']
    # filterset_fields = ['id']
    filterset_class= ReviewFilter
    ordering_fields = ['id']
    pagination_class = DefaultPagination

    def get_queryset(self):
        return Review.objects.filter(movie_id=self.kwargs['movie_pk'])
    
    def get_serializer_context(self):
        return {'movie_id':self.kwargs['movie_pk']}
    
    def destroy(self, request, *args, **kwargs):
        if Movie.objects.filter(review=kwargs['pk']).count() > 0:
            return Response({'error':'This review is associated with a movie item'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        if Viewer.objects.filter(review=kwargs['pk']).count() > 0:
            return Response({'error':'This review is associated with a viewer'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)
    
    def get_serializer_class(self):
        if self.request.method=='POST':
            return CreateReview
        if self.request.method=='PATCH':
            return UpdateReview
        return ReviewSerializer
 
class TriggerViewSet(ModelViewSet):
    queryset = Trigger.objects.all()
    serializer_class = TriggerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', 'description']
    filterset_fields = ['name']
    ordering_fields = ['name']
    # custom pagination
    pagination_class = DefaultPagination
    def destroy(self, request, *args, **kwargs):
        if Movie.objects.filter(trigger=kwargs['pk']).count() > 0:
            return Response({'error':'This trigger is associated with a movie item'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)
    

class GenreViewSet(ModelViewSet):
    # here it uses the normal pagination
    queryset = Genre.objects.all()
    http_method_names=['get','delete']
    serializer_class = GenreSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['genre']
    filterset_fields = ['genre']
    ordering_fields = ['genre']

    def destroy(self, request, *args, **kwargs):
        if Movie.objects.filter(genre=kwargs['pk']).count() > 0:
            return Response({'error':'This genre is associated with a movie item'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)
    


class ListViewSet(ModelViewSet):
    queryset = List.objects.all().select_related('viewer')
    serializer_class = ListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', 'description']
    filterset_fields = ['name']
    ordering_fields = ['name']


    def destroy(self, request, *args, **kwargs):
        if Movie.objects.filter(list=kwargs['pk']).count() > 0:
            return Response({'error':'This list is associated with a movie item'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)
    

    def get_serializer_class(self):
        if self.request.method=='POST':
            return UpdateRList
        if self.request.method=='PUT':
            return UpdateRList
        return ListSerializer
        
       
class ViewerViewSet(ModelViewSet):
    queryset = Viewer.objects.all()
    serializer_class = ViewerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['id', 'email']
    filterset_fields = ['email']
    ordering_fields = ['id']
    pagination_class = DefaultPagination

    def destroy(self, request, *args, **kwargs):
        if List.objects.filter(viewer=kwargs['pk']).count() > 0:
            return Response({'error':'This viewer is associated with a list item'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        if Review.objects.filter(Viewer=kwargs['pk']).count() > 0:
            return Response({'error':'This viewer is associated with a review item'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)
    

# ________________________________________________________________________________________________________________

# def ViewPage(request):
#     queryset = Movie.objects.all()
#     list(queryset)
#     return render(request,'MovieTriggerApp/index.html',{'name':'This is our Movie list  ','queryset':queryset})

# FUNCTION BASED
# @api_view(['GET','POST'])
# def MovieList(request):
#     if request.method=='GET':
#         #  we used select related to avoid over spanning the classes and taking long time
#         queryset = Movie.objects.all()
#         #  for the hyperlink we need an extra step 
#         serlizer = MovieSerlizer(queryset,many =True,context = {'request':request})
#         return Response(serlizer.data)
#     elif request.method =='POST':
#         #  we will create a new product
#         #  i will get it as a JSON object and i have to convert it to model
#         # deserlize
#         serlizer = MovieSerlizer(data = request.data)
#         #  we have to check is valid before accessing the data 
#         serlizer.is_valid(raise_exception=True)
#         # this will save it to the database 
#         serlizer.save()
#         return Response(serlizer.data,status=status.HTTP_201_CREATED)
    


# @api_view(['GET','PUT','DELETE'])
# def MovieDetail(request,id): 
#     # AN api should not give me an error it should give me a status
#     movie = get_object_or_404(Movie,pk=id)
#     lookup_field = ['id']
#     if request.method == 'GET':
#         serlizers = MovieSerlizer(movie,context = {'request':request})
#         return Response(serlizers.data)
#     elif request.method =='PUT':
#         # we will update the whole movies dict
#         serlizer = MovieSerlizer(movie,data = request.data)
#         serlizer.is_valid(raise_exception=True)
#         serlizer.save()
#         return Response(serlizer.data)
#     elif request.method =='DELETE':
#         # WE WANT TO DELETE A PRODUCT
#         if movie.list_set.count()>0:
#             return Response({'error':'This movie is associated with a list '},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    



# @api_view(['GET'])
# def List_of_Lists(request):
#     if request.method=='GET':
#         #  we used select related to avoid over spanning the classes and taking long time
#         queryset = List.objects.all()
#         #  for the hyperlink we need an extra step 
#         serlizer = ListSerlizer(queryset,many =True)
#         return Response(serlizer.data)


# @api_view()
# def trigger_list(request):
#     if request.method=='GET':
#         #  we used select related to avoid over spanning the classes and taking long time
#         queryset = Trigger.objects.all()
#         serlizer = TriggerSerlizer(queryset,many =True)
#         return Response(serlizer.data)


# @api_view()
# def trigger_details(request,pk):
#     trigger = get_object_or_404(Trigger,pk=pk)
#     if request.method == 'GET':
#         serlizers = TriggerSerlizer(trigger)
#         return Response(serlizers.data)
#     elif request.method =='PUT':
#         # we will update the whole trigger dict
#         serlizer = TriggerSerlizer(trigger,data = request.data)
#         serlizer.is_valid(raise_exception=True)
#         serlizer.save()
#         return Response(serlizer.data)
#     elif request.method =='DELETE':
#         # WE WANT TO DELETE A TRIIGGER
#         if trigger.movie_set.count()>0:
#             return Response({'error':'This trigger is associated with a movie '},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         trigger.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view()
# def review_list(request):
#     if request.method=='GET':
#         #  we used select related to avoid over spanning the classes and taking long time
#         queryset = Review.objects.all()
#         serlizer = ReviewSerlizer(queryset,many =True)
#         return Response(serlizer.data)