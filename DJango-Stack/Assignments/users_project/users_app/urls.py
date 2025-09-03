from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), # main page showing the users
    path("add_user/", views.add_user, name="add_user"), # from POST endpoint
]