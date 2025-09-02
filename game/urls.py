from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"), # main game page
    path('process_money/', views.process_money, name = "process_money"), #gold actions
    path('reset/', views.reset, name = "reset"), # to reset the game
]