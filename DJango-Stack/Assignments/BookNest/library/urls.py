from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import HomeView, RegisterView, AddBookView, BookDetailView, EditBookView, DeleteBookView, ToggleLikeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(template_name="library/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
    path("add/", AddBookView.as_view(), name="add_book"),
    path("book/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("book/<int:pk>/edit/", EditBookView.as_view(), name="edit_book"),
    path("book/<int:pk>/delete/", DeleteBookView.as_view(), name="delete_book"),
    path("book/<int:pk>/toggle-like/", ToggleLikeView.as_view(), name="toggle_like"),
]
