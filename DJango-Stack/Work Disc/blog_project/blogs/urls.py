from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blogs'),
    path('create/', views.create_blog, name='create_blog'),
    path('edit/<int:id>/', views.edit_blog, name='edit_blog'),
    path('update/<int:id>/', views.update_blog, name='update_blog'),
    path('delete/<int:id>/', views.delete_blog, name='delete_blog'),

    path('comment/create/<int:blog_id>/', views.create_comment, name='create_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),

    path('admins/', views.admin_list, name='admin_list'),
    path('admins/create/', views.create_admin, name='create_admin'),
]
