from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:course_id>/', views.delete_course, name='delete_course'),
    path('comment/<int:course_id>/', views.comment_course, name='comment_course'),
]