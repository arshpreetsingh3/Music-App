from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .models import Album 
from . import views

app_name ='music'
urlpatterns = [
    #/music/
    path('',views.IndexView.as_view(),name='index'), 

    path('register/',views.UserFormView.as_view(),name='register'),    

    #/music/album-id/
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),

    #/music/album/add
    path('album/add/',views.AlbumCreate.as_view(), name='album-add'),
    
    #/music/album/2 = means for updating album with pk of 2 
    path('album/<int:pk>/',views.AlbumUpdate.as_view(), name='album-update'),

     #/music/album/2/delete = this  if for deleting
    path('album/<int:pk>/delete/',views.AlbumDelete.as_view(), name='album-delete'),

    #musoic/albu-id/favorite/
    #path('<int:album_id>/favorite/', favorite, name="favorite"),
]
# $ denotes ending