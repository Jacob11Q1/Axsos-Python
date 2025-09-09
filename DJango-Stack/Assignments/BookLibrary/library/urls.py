from django.urls import path
from . import views

urlpatterns = [
    # Home Redirect
    path('', views.home, name='home'),  # root URL
    
    # Auth
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Books
    path('books/', views.book_list, name='book_list'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),

    # Favorites
    path('books/<int:book_id>/favorite/', views.favorite_book, name='favorite_book'),
    path('books/<int:book_id>/unfavorite/', views.unfavorite_book, name='unfavorite_book'),

    # Profile page (Sensei Bonus 🚀)
    path('users/<int:user_id>/', views.user_profile, name='user_profile'),
]

