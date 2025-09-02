from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root route for Ninja Gold page
    path('process_money/', views.process_money, name='process_money'),  # Process gold
]