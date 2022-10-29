from django.urls import path

from reviewer import views

app_name = "reviewer"
urlpatterns = [
    path("reviewers", views.reviewers, name="reviewer-list"),
]
