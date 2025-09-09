from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import User, Book
from .forms import RegisterForm, LoginForm, BookForm

# ------------------------------
# HOME REDIRECT
# ------------------------------

def home(request):
    return render(request, 'library/home.html')

# ------------------------------
# AUTHENTICATION VIEWS
# ------------------------------

def register(request):
    """Register a new user"""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # save user to database
            login(request, user)  # log them in automatically
            messages.success(request, "Registration successful!")
            return redirect('book_list')
        else:
            # Show form errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = RegisterForm()
    return render(request, 'library/register.html', {'form': form})

def login_view(request):
    """Login existing user"""
    next_url = request.GET.get('next', '')  # Capture the page user was trying to access

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully!")

            # Redirect to next_url if it exists, otherwise default
            redirect_to = request.POST.get('next') or 'book_list'
            return redirect(redirect_to)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = LoginForm()

    return render(request, 'library/login.html', {'form': form, 'next': next_url})


@login_required
def logout_view(request):
    """Logout user"""
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')


# ------------------------------
# BOOK VIEWS
# ------------------------------

@login_required
def book_list(request):
    """Main page: show all books"""
    books = Book.objects.all().order_by('-created_at')  # newest first
    return render(request, 'library/books.html', {'books': books})

@login_required
def add_book(request):
    """Add a new book"""
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            new_book = form.save(commit=False)  # don't save yet
            new_book.uploaded_by = request.user  # link uploader
            new_book.save()  # save to database
            new_book.users_who_like.add(request.user)  # auto favorite
            messages.success(request, "Book added successfully!")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    return redirect('book_list')

@login_required
def book_detail(request, book_id):
    """Show single book details and users who favorited it"""
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'library/book_detail.html', {'book': book})

@login_required
def edit_book(request, book_id):
    """Edit a book (only uploader can edit)"""
    book = get_object_or_404(Book, id=book_id)
    if book.uploaded_by != request.user:
        messages.error(request, "You cannot edit this book.")
        return redirect('book_list')

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully!")
            return redirect('book_detail', book_id=book.id)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = BookForm(instance=book)

    return render(request, 'library/add_edit_book.html', {'form': form, 'book': book})

@login_required
def delete_book(request, book_id):
    """Delete a book (only uploader can delete)"""
    book = get_object_or_404(Book, id=book_id)
    if book.uploaded_by != request.user:
        messages.error(request, "You cannot delete this book.")
    else:
        book.delete()
        messages.success(request, "Book deleted successfully!")
    return redirect('book_list')


# ------------------------------
# FAVORITE / UNFAVORITE VIEWS
# ------------------------------

@login_required
def favorite_book(request, book_id):
    """Add book to user's favorites"""
    book = get_object_or_404(Book, id=book_id)
    book.users_who_like.add(request.user)
    messages.success(request, f"Added '{book.title}' to your favorites!")
    return redirect('book_list')

@login_required
def unfavorite_book(request, book_id):
    """Remove book from user's favorites"""
    book = get_object_or_404(Book, id=book_id)
    book.users_who_like.remove(request.user)
    messages.success(request, f"Removed '{book.title}' from your favorites!")
    return redirect('book_list')


# ------------------------------
# USER PROFILE VIEW (Sensei Bonus)
# ------------------------------

@login_required
def user_profile(request, user_id):
    """Show user's profile and their favorite books"""
    user_profile = get_object_or_404(User, id=user_id)
    return render(request, 'library/profile.html', {'user_profile': user_profile})
