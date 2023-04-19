from django.urls import path, include
from . import views 
from django.contrib import admin
from rest_framework.routers import SimpleRouter


# define routers
router = SimpleRouter()
router.register('movies', views.MovieViewSet)
router.register('reviews', views.ReviewViewSet)
router.register('triggers', views.TriggerViewSet)
router.register('lists', views.ListViewSet)
router.register('viewers', views.ViewerViewSet)
router.register('genres', views.GenreViewSet)


urlpatterns = [
    path('admin/',admin.site.urls),
    #path('MovieTriggerProject/',views.ViewPage),
    path('', include(router.urls))
    #  to view the movies in the api 
    # path('movies/',views.MovieList),
    # to view each movie seperatly
    # path('movies/<int:id>',views.MovieDetail),
    # path('lists/',views.List_of_Lists),
    # path('triggers/',views.trigger_list),



    # hyperlink related fields
    # path('triggers/<int:pk>',views.trigger_details,name='trigger-details'),
    # path('reviews/',views.review_list)
]