from django.shortcuts import render , redirect
import random

# Create your views here.

# Main page function
def index(request):
    # To initialize the session variables if the don't exist yet
    if "gold" not in request.session:
        request.session["gold"] = 0
        request.session['activities'] = []
    context = {
        'gold': request.session['gold'],
        'activities': request.session['activities'],
    }
    return render(request, 'game/index.html', context)

# To handle the gold earning method
def process_money(request):
    location = request.POST.get('location')
    if location:
        if location == 'farm':
            gold_earned = random.randint(10, 20)
        elif location == 'cave':
            gold_earned = random.randint(5, 10)
        elif location == 'house':
            gold_earned = random.randint(2, 5)
        elif location == 'quest':
            gold_earned = random.randint(-50, 50)
        else:
            gold_earned = 0

        request.session['gold'] += gold_earned
        request.session['activities'].append(f"Visited {location.capitalize()}: {gold_earned} gold")
    return redirect('index')

# Reseting the game
def reset(request):
    request.session.flush() # clears all session data
    return redirect("index")
