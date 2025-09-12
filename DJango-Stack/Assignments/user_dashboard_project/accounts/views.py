"""Views for registration and dashboard pages."""

from django.shortcuts import render, redirect  # helper shortcuts
from .forms import RegisterForm, CustomLoginForm  # import our forms
from django.contrib.auth.decorators import login_required  # decorator to require login
from django.contrib import messages  # messaging framework for flash messages
from django.contrib.auth import login as auth_login  # programmatically log user in

# Create your views here.

def register_view(request):
    """
    Handle GET and POST for registration.
    On GET: show empty form.
    On POST: validate, save user, log them in, redirect to dashboard.
    """
    if request.method == "POST":
        form = RegisterForm(request.POST)  # populate form with POST data
        if form.is_valid():  # if all validation passes
            user = form.save()  # create user
            auth_login(request, user)  # log user in directly
            messages.success(request, "Registration successful. Welcome!")  # success message
            return redirect("accounts:dashboard")  # go to dashboard
        else:
            messages.error(request, "Please fix the errors below.")  # error message
    else:
        form = RegisterForm()  # empty form for GET

    # render the registration template with form in context
    return render(request, "accounts/register.html", {"form": form})

@login_required  # ensure only logged-in users can access dashboard
def dashboard_view(request):
    """
    Simple dashboard view that shows user info, hover cards, and sample stats.
    The template will use Bootstrap cards and CSS animations for a SaaS feel.
    """
    user = request.user  # currently logged-in user
    # sample data to populate dashboard (replace with real data later)
    cards = [
        {"title": "Projects", "value": 12, "desc": "Active projects you manage"},
        {"title": "Members", "value": 34, "desc": "Team members across projects"},
        {"title": "Tasks", "value": 128, "desc": "Open tasks assigned to you"},
    ]

    # render dashboard template with user and sample cards
    return render(request, "accounts/dashboard.html", {"user": user, "cards": cards})
