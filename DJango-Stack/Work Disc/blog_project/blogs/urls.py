from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blogs'),
    path('create/', views.create, name='create_blog'),
    path('edit/<int:id>/', views.edit, name='edit_blog'),
    path('update/<int:id>/', views.update, name='update_blog'),
    path('delete/<int:id>/', views.delete, name='delete_blog'),

    # Comments
    path('comment/create/<int:blog_id>/', views.create_comment, name='create_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
