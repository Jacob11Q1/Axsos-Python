"""
URL configuration for user_dashboard_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""Project-level URL configuration that routes to app URLs and admin."""

from django.contrib import admin  # admin site
from django.urls import path, include  # include() to include app urls

urlpatterns = [
    path("admin/", admin.site.urls), # admin panel
    path("", include("accounts.urls", namespace="accounts")),  # include accounts app URLs as root
]