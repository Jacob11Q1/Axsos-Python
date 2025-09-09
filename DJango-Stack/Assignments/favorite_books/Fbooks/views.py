from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.db.models import Q
from django.contrib import messages

from .models import Book, User
from .forms import BookForm, CustomUserCreationForm

# Home page with search & pagination
class HomeView(ListView):
    model = Book
    template_name = "Fbooks/home.html"
    context_object_name = "books"
    paginate_by = 6  # 6 books per page

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        books = Book.objects.select_related('uploaded_by').all().order_by('-created_at')
        if query:
            books = books.filter(Q(title__icontains=query) | Q(uploaded_by__username__icontains=query))
        return books

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context

# Add book
class AddBookView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = "Fbooks/add_book.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        messages.success(self.request, "Book added successfully!")
        return super().form_valid(form)

# Profile page
class ProfileView(DetailView):
    model = User
    template_name = "Fbooks/profile.html"
    context_object_name = "user_profile"
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = self.get_object()
        context['uploaded_books'] = user_profile.books_uploaded.prefetch_related('users_who_like').all()
        context['liked_books'] = user_profile.liked_books.select_related('uploaded_by').all()
        return context

# Registration
class RegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'Fbooks/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, "Account created successfully!")
        return super().form_valid(form)

# AJAX Like/Unlike
from django.views import View

class LikeBookAjaxView(LoginRequiredMixin, View):
    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        user = request.user
        liked = False

        if book.users_who_like.filter(id=user.id).exists():
            book.users_who_like.remove(user)
        else:
            book.users_who_like.add(user)
            liked = True

        return JsonResponse({
            "liked": liked,
            "likes_count": book.users_who_like.count()
        })
