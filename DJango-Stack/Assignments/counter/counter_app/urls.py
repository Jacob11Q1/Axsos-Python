from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index, name = "index"), # this is the root
    path('destroy_session/', views.destroy, name = "destroy"), # This for the reset
]