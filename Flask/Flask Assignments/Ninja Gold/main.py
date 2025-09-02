from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"


BUILDINGS = {
    "farm": (10, 20),
    "cave": (5, 10),
    "house": (2, 5),
    "casino": (-50, 50)
}

# Root route
@app.route('/')
def index():
    # Initialize session variables
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []
        session['moves'] = 0
        session['game_over'] = False
        session['win'] = False
    return render_template("index.html", gold=session['gold'], activities=session['activities'], game_over=session['game_over'], win=session['win'])

# Process money route
@app.route('/process_money', methods=['POST'])
def process_money():
    if session.get('game_over', False):
        return redirect('/')

    building = request.form.get('building')
    min_gold, max_gold = BUILDINGS.get(building, (0,0))
    earned = random.randint(min_gold, max_gold)

    # Update session gold and moves
    session['gold'] += earned
    session['moves'] += 1

    
    time = datetime.now().strftime("%Y/%m/%d %I:%M %p")
    if earned >= 0:
        message = f"Earned {earned} gold from the {building}! ({time})"
        color = "green"
    else:
        message = f"Entered a {building} and lost {abs(earned)} gold... Ouch! ({time})"
        color = "red"

    session['activities'].insert(0, {"message": message, "color": color})

    
    if session['gold'] >= 500 and session['moves'] <= 15:
        session['game_over'] = True
        session['win'] = True
        session['activities'].insert(0, {"message": "You won!", "color": "blue"})
    elif session['moves'] >= 15 and session['gold'] < 500:
        session['game_over'] = True
        session['win'] = False
        session['activities'].insert(0, {"message": "You lost!", "color": "blue"})

    return redirect('/')

# Reset game
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)