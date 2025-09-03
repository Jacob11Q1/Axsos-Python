from django.shortcuts import render ,redirect
from .models import User

# Create your views here.

# Display all users and the Add User form
def index(request):
    users = User.objects.all() # to get all the users from the DataBase
    return render(request, "users_app/index.html", {"users": users})

# Handling the add Users from the submission
def add_user(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        
        # Creating a new user and save it to DB
        User.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            age = age
        )
        
        return redirect('/') # Redirect to main page after adding user