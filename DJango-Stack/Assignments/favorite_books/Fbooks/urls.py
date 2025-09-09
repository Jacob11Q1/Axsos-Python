from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import HomeView, AddBookView, ProfileView, RegisterView, LikeBookAjaxView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add/', AddBookView.as_view(), name='add_book'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='Fbooks/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('like/<int:book_id>/', LikeBookAjaxView.as_view(), name='like_book_ajax'),
]
