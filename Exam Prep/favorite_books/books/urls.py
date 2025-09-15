from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('add_book/', views.add_book, name="add_book"),
    path('like/<int:book_id>/', views.like_book, name="like_book"),
    path('unlike/<int:book_id>/', views.unlike_book, name="unlike_book"),
    path('edit/<int:book_id>/', views.edit_book, name="edit_book"),
    path('delete/<int:book_id>/', views.delete_book, name="delete_book"),
    path('profile/<int:user_id>/', views.profile, name="profile"),
]
