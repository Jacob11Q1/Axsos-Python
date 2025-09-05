from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('little-books/', views.little_books, name='little_books'),
    path('books/author/', views.books_by_author, name='books_by_author'),
    path('exclude-example/', views.exclude_example, name='exclude_example'),

    # CRUD URLs
    path('book/add/', views.add_book, name='add_book'),
    path('author/add/', views.add_author, name='add_author'),
    path('book/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('book/<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
]
