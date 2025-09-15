from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import User, Book

# Create your views here.

def logged_in(request):
    return "user_id" in request.session

def current_user(request):
    return User.objects.get(id=request.session["user_id"])

# Auth
def index(request):
    return render(request, "books/index.html")

def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm = request.POST["confirm"]
        if password != confirm:
            messages.error(request, "Passwords do not match")
            return redirect("index")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("index")
        user = User(name=name, email=email)
        user.set_password(password)
        user.save()
        request.session["user_id"] = user.id
        messages.success(request, "Registration successful")
        return redirect("dashboard")

def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                request.session["user_id"] = user.id
                messages.success(request, "Welcome back!")
                return redirect("dashboard")
        except User.DoesNotExist:
            pass
        messages.error(request, "Invalid login")
        return redirect("index")

def logout(request):
    request.session.flush()
    messages.info(request, "Logged out successfully")
    return redirect("index")

# Books CRUD + Likes
def dashboard(request):
    if not logged_in(request):
        return redirect("index")
    user = current_user(request)
    books = Book.objects.all().order_by("-created_at")
    return render(request, "books/dashboard.html", {"user": user, "books": books})

def add_book(request):
    if not logged_in(request):
        return redirect("index")
    if request.method == "POST":
        user = current_user(request)
        title = request.POST["title"]
        desc = request.POST["desc"]
        if len(title) < 3 or len(desc) < 5:
            messages.error(request, "Title or description too short")
            return redirect("dashboard")
        Book.objects.create(title=title, desc=desc, uploaded_by=user)
        messages.success(request, "Book added successfully")
    return redirect("dashboard")

def like_book(request, book_id):
    if not logged_in(request):
        return redirect("index")
    user = current_user(request)
    book = Book.objects.get(id=book_id)
    if user not in book.liked_by.all():
        book.liked_by.add(user)
    return redirect("dashboard")

def unlike_book(request, book_id):
    if not logged_in(request):
        return redirect("index")
    user = current_user(request)
    book = Book.objects.get(id=book_id)
    if user in book.liked_by.all():
        book.liked_by.remove(user)
    return redirect("dashboard")

def edit_book(request, book_id):
    if not logged_in(request):
        return redirect("index")
    book = get_object_or_404(Book, id=book_id)
    user = current_user(request)
    if book.uploaded_by != user:
        messages.error(request, "Unauthorized")
        return redirect("dashboard")
    if request.method == "POST":
        book.title = request.POST["title"]
        book.desc = request.POST["desc"]
        book.save()
        messages.success(request, "Book updated")
        return redirect("dashboard")
    return render(request, "books/edit_book.html", {"book": book})

def delete_book(request, book_id):
    if not logged_in(request):
        return redirect("index")
    book = get_object_or_404(Book, id=book_id)
    user = current_user(request)
    if book.uploaded_by == user:
        book.delete()
        messages.success(request, "Book deleted")
    else:
        messages.error(request, "Unauthorized")
    return redirect("dashboard")

# Profile
def profile(request, user_id):
    if not logged_in(request):
        return redirect("index")
    profile_user = get_object_or_404(User, id=user_id)
    uploaded = profile_user.books.all()
    liked = profile_user.liked_books.all()
    return render(request, "books/profile.html", {
        "profile_user": profile_user,
        "uploaded": uploaded,
        "liked": liked
    })