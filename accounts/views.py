from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import JsonResponse
from .forms import RegisterForm, LoginForm
from .models import User




# ---------------- HOME ----------------
def home_view(request):
    return render(request, 'accounts/home.html')

# ---------------- REGISTER ----------------
def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


# ---------------- LOGIN ----------------
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, f"Welcome back, {user.first_name}!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid email or password")
    return render(request, 'accounts/login.html')


# ---------------- LOGOUT ----------------
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out")
    return render(request, 'accounts/logout.html')


# ---------------- DASHBOARD ----------------
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')


# ---------------- AJAX EMAIL CHECK ----------------
def check_email_view(request):
    email = request.GET.get('email', '').lower()
    exists = User.objects.filter(email=email).exists()
    return JsonResponse({'exists': exists})
