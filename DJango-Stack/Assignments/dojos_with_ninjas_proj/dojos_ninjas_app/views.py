from django.shortcuts import render, redirect
from .models import Dojo, Ninja

# Create your views here.

# Show the hompage with dojo and ninja list:
def index(request):
    context = {
        "all_dojos": Dojo.objects.all() # To Get all dojos (with thier ninjas)
    }
    
    return render(request, "dojos_ninjas_app/index.html", context)

# Create a new Dojo:
def create_dojo(request):
    if request.method == "POST":
        Dojo.objects.create(
            name = request.POST['name'],
            city = request.POST['city'],
            state = request.POST['state']
        )
    
    return redirect('/')

# Create a new Ninja:
def create_ninja(request):
    if request.method == "POST":
        dojo = Dojo.objects.get(id = request.POST['dojo_id'])
        Ninja.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            dojo = dojo
        )
    
    return redirect('/')

# Delete dojo (and all it's ninjas due to CASCADE in models):
def delete_dojo(request, dojo_id):
    dojo = Dojo.objects.get(id = dojo_id)
    dojo.delete()
    return redirect('/')