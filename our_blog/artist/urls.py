from django.urls import path

from artist import views

app_name = "artist"
urlpatterns = [
    path("artists/", views.ArtistListView.as_view(), name="artist-list"),
    path("artist/add/", views.ArtistCreateView.as_view(), name="artist-add"),
    path("artist/<int:pk>/detail/", views.ArtistDetailView.as_view(), name="artist-detail"),
    path("artist/<int:pk>/update/", views.ArtistUpdateView.as_view(), name="artist-update"),
    path("artist/<int:pk>/delete/", views.ArtistDeleteView.as_view(), name="artist-delete"),
]