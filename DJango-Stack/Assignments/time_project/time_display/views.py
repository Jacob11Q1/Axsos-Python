from django.shortcuts import render
from time import gmtime, strftime # Import gmtime for UTC time, strftime to format it

# Create your views here.

def index(request):
    # To get the current UTC time and format it as "YYYY-MM-DD HH:MM AM/PM"
    current_time = strftime("%Y-%m-%d %H:%M %p", gmtime())
    
    # Pass the data to the template
    context = {
        "time": current_time
    }
    # Render 'index.html' with the context data
    return render(request, 'index.html', context)