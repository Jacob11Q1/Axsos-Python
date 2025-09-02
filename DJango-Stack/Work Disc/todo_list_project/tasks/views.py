from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def create_user(request):
    if request.method == "POST":
        email = request.POST.get("email")  # safely get the email field from the form
        # For now, let's just confirm it's working
        return HttpResponse(f"User with email {email} created!")
    else:
        return redirect("index")  # redirect to home if accessed without POST