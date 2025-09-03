from django.shortcuts import render, redirect


# Create your views here.

# NINJA BONUS: root route uses /blogs method
def root_redirect(request):
    return redirect('/blogs')

# Display form to create a new user
def new_user(request):
    return render(request, 'users/new.html')


# Display login form
def login_user(request):
    return render(request, 'users/login.html')

# Display all users
def index_users(request):
    return render(request, 'users/index.html')
