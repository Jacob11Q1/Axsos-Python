from django.shortcuts import render , redirect
import random
# Create your views here.

# Root route - to display the game page:
def index(request):
    # To check if the number is already in the seesion(the first visit to the page)
    if "number" not in request.session:
        # make the user pick a number from 1 to 100
        request.session["number"] = random.randint(1,100)
        # To initialize the attempts counter
        request.session["attempts"] = 0
        # To initialize the message to show the feedback
        request.session["message"] = ""
        # To initialize the color of the message display
        request.session["color"] = "black"

    # Rendering the template:
    return render(request, "game/index.html")

# The route to handle the user's guess numbers
def guess(request):
    if request.method == "POST":
        # Get the user's to guess from the form and convert it to int
        guess = int(request.POST.get("guess", 0))
        request.session["attempts"] += 1 # Attempting to increase the counter
    
    # Comparing the quess with the random number:
    if guess < request.session["number"]:
        request.session["message"] = "Too low!"
        request.session["color"] = "blue"  # Message color
    elif guess > request.session["number"]:
        request.session["message"] = "Too high!"
        request.session["color"] = "red"
    else:
        # Correct guess
        request.session["message"] = f"Correct! You got it in {request.session['attempts']} attempts."
        request.session["color"] = "green"
    
    # Redirect back to the main page to show updated message
    return redirect("index")

# The Route to reset the game:
def reset(request):
    # Clear all session data using the (flush)
    request.session.flush()
    # Directing back to the root route to start a new game
    return redirect("index")