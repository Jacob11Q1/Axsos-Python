from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.contrib.auth.hashers import make_password, check_password
from datetime import date
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'login_app/index.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_pw = request.POST['confirm_pw']
        birthday = request.POST.get('birthday')
        
        errors = []
        
        # Validations:
        if len(first_name) < 2 or not first_name.isalpha():
            errors.append("First name must be at least 2 letters and contain letters only")
        if len(last_name) < 2 or not last_name.isalpha():
            errors.append("Last name must be at least 2 letters and contain letters only")
        if len(password) < 8:
            errors.append("Password must be at least 8 characters")
        if password != confirm_pw:
            errors.append("Passwords must match")
        if birthday:
            try:
                bday = date.fromisoformat(birthday)
                if bday >= date.today():
                    errors.append("Birthday must be in the past")
                # Sensei bonus: age >= 13
                age = date.today().year - bday.year - ((date.today().month, date.today().day) < (bday.month, bday.day))
                if age < 13:
                    errors.append("You must be at least 13 years old to register")
            except:
                errors.append("Invalid birthday format")
        # Email uniqueness
        if User.objects.filter(email=email):
            errors.append("Email already exists")

        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('/')
        else:
            hashed_pw = make_password(password)
            user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=hashed_pw, birthday=birthday)
            request.session['user_id'] = user.id
            messages.success(request, f"Welcome {user.first_name}!")
            return redirect('/success')
    return redirect('/')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                messages.success(request, f"Welcome back {user.first_name}!")
                return redirect('/success')
            else:
                messages.error(request, "Incorrect password")
        except User.DoesNotExist:
            messages.error(request, "Email not found")
    return redirect('/')

def success(request):
    if 'user_id' not in request.session:
        messages.error(request, "You must log in first")
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    return render(request, 'login_app/success.html', {'user': user})

def logout(request):
    request.session.flush()
    messages.info(request, "Logged out successfully")
    return redirect('/')

def check_email(request):
    email = request.GET.get('email')
    exists = User.objects.filter(email=email).exists()
    return JsonResponse({'exists': exists})