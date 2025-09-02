from django.shortcuts import render , redirect

# Create your views here.

def index(request):
    # To check if Counter exsists in the session
    if 'counter' not in request.session:
        request.session['counter'] = 0
    # To initialize the session variables if they dont exist
    if 'sensi' not in request.session:
        request.session['sensi'] = 1 # A default multiplier
    if 'bonus' not in request.session:
        request.session['bonus'] = 0
    
    # This to handle the button click
    if request.method == 'POST' and 'click' in request.POST:
        request.session['counter'] += request.session['sensi']
    
    context = {
        'counter': request.session['counter'],
        'sensi': request.session['sensi'],
        'bonus': request.session['bonus']
    }
    return render(request, 'counter_app/index.html', context)

def destroy(request):
    if request.method == 'POST':
        request.session.flush() # To clear all session data
    return redirect("index")