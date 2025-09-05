from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Author
from .forms import BookForm
from .AuthorForm import AuthorForm

# Home page
def home(request):
    books = Book.objects.all()
    return render(request, 'library_app/home.html', {'books': books})

# Books starting with "Little"
def little_books(request):
    books = Book.objects.filter(title__startswith='Little')
    return render(request, 'library_app/home.html', {'books': books})

# Books by author starting with "Al"
def books_by_author(request):
    books = Book.objects.filter(authors__name__startswith='Al')
    return render(request, 'library_app/home.html', {'books': books})

# Example exclude
def exclude_example(request):
    books = Book.objects.exclude(title__icontains='The')
    return render(request, 'library_app/home.html', {'books': books})

# ---------------- CRUD ----------------

# Add book
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'library_app/book_form.html', {'form': form})

# Edit book
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm(instance=book)
    return render(request, 'library_app/book_form.html', {'form': form})

# Delete book
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    return render(request, 'library_app/book_confirm_delete.html', {'book': book})

# Book detail
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'library_app/book_detail.html', {'book': book})


# Author Form To Add Author
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # back to homepage
    else:
        form = AuthorForm()
    return render(request, 'library_app/author_form.html', {'form': form})