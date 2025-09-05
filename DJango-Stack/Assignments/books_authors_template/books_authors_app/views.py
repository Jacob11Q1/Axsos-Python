from django.shortcuts import render , redirect , get_object_or_404
from .models import Book, Author

# Create your views here.

def home(request):
    return render(request, "books_authors_app/home.html")

# ----- Book Views -----

# List of all books + create book:
def books_list_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        if title and description:
            Book.objects.create(title = title, description = description) # Create new book
        return redirect('books_list_create')  # Redirect to refresh page
    books = Book.objects.all()  # Fetch all books
    return render(request, "books_authors_app/books.html", {"books": books})

# Book details page + add author:
def book_detail(request, book_id):
    book = get_object_or_404(Book, id = book_id)
    
    # Bonus Show only authors that are not yet associated:
    available_authors = Author.objects.exclude(id__in = book.authors.all())
    
    if request.method == "POST":
        author_id = request.POST.get("author")
        if author_id:
            author = Author.objects.get(id = author_id)
            book.authors.add(author) # Add the author to this book
        return redirect(request, 'book_detail', book_id = book.id)

    return render(request, "books_authors_app/book_detail.html", {
        "book": book,
        "available_authors": available_authors
    })

# ----- Author View -----

# List all authors + create author:
def authors_list_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            Author.objects.create(name = name)
        return redirect('authors_list_create')

    authors = Author.objects.all()
    return render(request, "books_authors_app/authors.html", {"authors": authors})


# Author detail page + add book
def author_detail(request, author_id):
    author = get_object_or_404(Author, id = author_id)

    # Bonus: Only show books not yet associated
    available_books = Book.objects.exclude(id__in = author.books.all())

    if request.method == "POST":
        book_id = request.POST.get("book")
        if book_id:
            book = Book.objects.get(id = book_id)
            author.books.add(book)
        return redirect('author_detail', author_id = author.id)

    return render(request, "books_authors_app/author_detail.html", {
        "author": author,
        "available_books": available_books
    })