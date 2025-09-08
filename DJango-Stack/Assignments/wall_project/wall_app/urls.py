from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall, name='wall'),
    path('add_message/', views.add_message, name='add_message'),
    path('add_comment/<int:message_id>/', views.add_comment, name='add_comment'),
    path('delete_message/<int:message_id>/', views.delete_message, name='delete_message'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]