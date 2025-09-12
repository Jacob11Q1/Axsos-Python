from django.urls import path
from .views import register_view, login_view, logout_view, dashboard_view, check_email_view
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # root path
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('check_email/', check_email_view, name='check_email'),
]
