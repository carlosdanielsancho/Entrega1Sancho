from django.urls import path

from home import views

app_name = "home"
urlpatterns = [
    path("", view=views.index, name="index"),
]