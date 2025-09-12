"""App-level URLs for accounts app (register, login, logout, dashboard)."""

from django.urls import path  # path for URL patterns
from . import views  # import views from current app
from django.contrib.auth import views as auth_views  # built-in auth views for login/logout

app_name = "accounts"  # namespace for URLs

urlpatterns = [
    path("register/", views.register_view, name="register"),  # user registration page
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html",
                                                authentication_form=views.CustomLoginForm), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),  # logout
    path("", views.dashboard_view, name="dashboard"),  # dashboard (root)
]