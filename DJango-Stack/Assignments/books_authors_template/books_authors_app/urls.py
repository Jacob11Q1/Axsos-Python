from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books_list_create, name='books_list_create'),       # List & create books
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),      # Book detail page
    path('authors/', views.authors_list_create, name='authors_list_create'),  # List & create authors
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'), # Author detail page
]