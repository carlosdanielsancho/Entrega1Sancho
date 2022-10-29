from django.urls import path

from album import views

app_name = "album"
urlpatterns = [
    path("albums", views.albums, name="album-list"),
    path("album/add", views.create_album, name="album-add"),
]