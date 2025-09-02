from django.shortcuts import render , redirect
import random
from datetime import datetime

# Create your views here.

# Main page
def index(request):
    # Initialize session variables if they don't exist
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []

    context = {
        'gold': request.session['gold'],
        'activities': request.session['activities']
    }
    return render(request, 'ninja/index.html', context)

def process_money(request):
    if request.method == 'POST':
        location = request.POST['location']
        gold_earned = 0

        # Determine gold earned/lost based on location
        if location == 'farm':
            gold_earned = random.randint(10, 20)
        elif location == 'cave':
            gold_earned = random.randint(5, 10)
        elif location == 'house':
            gold_earned = random.randint(2, 5)
        elif location == 'quest':
            gold_earned = random.randint(-50, 50)

        # Update session gold
        request.session['gold'] += gold_earned

        # Add activity log
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if gold_earned >= 0:
            message = f"Earned {gold_earned} gold from the {location}! ({now})"
        else:
            message = f"Lost {abs(gold_earned)} gold from the {location}... Ouch! ({now})"

        # Save to session
        activities = request.session['activities']
        activities.insert(0, message)  # latest on top
        request.session['activities'] = activities

    return redirect('/')