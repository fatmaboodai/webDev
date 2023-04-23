from django.urls import path, include
from . import views 
from django.contrib import admin
from rest_framework.routers import SimpleRouter,DefaultRouter
from rest_framework_nested import routers


# define routers
router = routers.DefaultRouter()
router.register('movies', views.MovieViewSet)
router.register('reviews', views.ReviewViewSet,basename='movie-detail')
router.register('triggers', views.TriggerViewSet)
router.register('lists', views.ListViewSet)
router.register('viewers', views.ViewerViewSet)
router.register('genres', views.GenreViewSet)
# router.register('triggers',views.TriggerViewSet,basename='trigger-details')


movie_router = routers.NestedDefaultRouter(router,'movies',lookup='movie')
movie_router.register('reviews',views.ReviewViewSet,basename='movie-review')

movie_viewer = routers.NestedDefaultRouter(router,'viewers',lookup='viewer')
movie_viewer.register('reviews',views.ReviewViewSet,basename='viewer-review')


urlpatterns = router.urls+movie_router.urls+movie_viewer.urls




# urlpatterns = [
    # path('admin/',admin.site.urls),
    # path('MovieTriggerProject/',views.ViewPage),
    # path('', include(router.urls))
    #  to view the movies in the api 
    # path('movies/',views.MovieList),
    # to view each movie seperatly
    # path('movies/<int:id>',views.MovieDetail),
    # path('lists/',views.List_of_Lists),
    # path('triggers/',views.trigger_list),

    # hyperlink related fields
    # path('triggers/',views.TriggerViewSet,name='trigger-details'),
    # path('reviews/',views.review_list)
# ]