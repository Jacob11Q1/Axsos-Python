from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, View
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import JsonResponse, HttpResponseForbidden
from django.db.models import Q
from django.contrib.auth import login
from .models import Book
from .forms import BookForm, CustomUserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class HomeView(ListView):
    model = Book
    template_name = "library/home.html"
    context_object_name = "books"
    paginate_by = 6

    def get_queryset(self):
        q = self.request.GET.get("q", "")
        qs = Book.objects.select_related("uploaded_by").all()
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(uploaded_by__username__icontains=q))
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["query"] = self.request.GET.get("q", "")
        return ctx

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "library/register.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, "Account created. You are now logged in.")
        login(self.request, user)
        return redirect(self.success_url)

class AddBookView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = "library/add_book.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        response = super().form_valid(form)
        # auto-favorite by uploader
        self.object.users_who_like.add(self.request.user)
        messages.success(self.request, "Book added and favorited.")
        return response

class BookDetailView(DetailView):
    model = Book
    template_name = "library/book_detail.html"
    context_object_name = "book"

class EditBookView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = "library/edit_book.html"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != request.user:
            return HttpResponseForbidden("You cannot edit this book.")
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, "Book updated.")
        return reverse("book_detail", kwargs={"pk": self.object.pk})

class DeleteBookView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = "library/delete_book.html"
    success_url = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.uploaded_by != request.user:
            return HttpResponseForbidden("You cannot delete this book.")
        return super().dispatch(request, *args, **kwargs)

class ToggleLikeView(LoginRequiredMixin, View):
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        user = request.user
        liked = False
        if book.users_who_like.filter(pk=user.pk).exists():
            book.users_who_like.remove(user)
        else:
            book.users_who_like.add(user)
            liked = True
        return JsonResponse({"liked": liked, "likes_count": book.users_who_like.count()})
