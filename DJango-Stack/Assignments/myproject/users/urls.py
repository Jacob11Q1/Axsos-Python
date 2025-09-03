from django.urls import path
from . import views

urlpatterns = [
    path('', views.root_redirect),      # Root route `/` → redirects to /blogs
    path('register/', views.new_user),  # /register
    path('login/', views.login_user),   # /login
    path('users/new/', views.new_user), # /users/new
    path('users/', views.index_users),  # /users
]