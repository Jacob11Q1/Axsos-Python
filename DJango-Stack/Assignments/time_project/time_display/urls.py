from django.urls import path
from . import views # Import views from this app

urlpatterns = [
    path('', views.index, name='index'), # Root path ('') points to the index view
    path('time_display/', views.index, name='time_display'), # Optional path '/time_display/' also points to the same index view
]