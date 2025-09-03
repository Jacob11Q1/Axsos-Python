from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),       # /surveys
    path('new/', views.new),     # /surveys/new
]