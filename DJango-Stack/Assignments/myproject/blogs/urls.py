from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),                       # /blogs
    path('new/', views.new),                     # /blogs/new
    path('create/', views.create),               # /blogs/create
    path('<int:number>/', views.show),           # /blogs/<number>
    path('<int:number>/edit/', views.edit),      # /blogs/<number>/edit
    path('<int:number>/delete/', views.destroy), # /blogs/<number>/delete
]