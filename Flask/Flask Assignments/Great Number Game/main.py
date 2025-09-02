from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"

leaderboard = []

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['attempts'] = 0
        session['status'] = ""
    return render_template('index.html', status=session['status'], attempts=session['attempts'])

@app.route('/guess', methods=['POST'])
def guess():
    try:
        guess = int(request.form['guess'])
    except ValueError:
        session['status'] = "invalid"
        return redirect(url_for('index'))

    session['attempts'] += 1

    if session['attempts'] > 5:
        session['status'] = "lose"
        return redirect(url_for('index'))

    if guess < session['number']:
        session['status'] = "low"
    elif guess > session['number']:
        session['status'] = "high"
    else:
        session['status'] = "correct"

    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

@app.route('/save_winner', methods=['POST'])
def save_winner():
    name = request.form['name']
    leaderboard.append({
        "name": name,
        "attempts": session['attempts']
    })
    session.clear()
    return redirect(url_for('leaderboard_page'))

@app.route('/leaderboard')
def leaderboard_page():
    sorted_board = sorted(leaderboard, key=lambda x: x['attempts'])
    return render_template('leaderboard.html', leaderboard=sorted_board)

if __name__ == "__main__":
    app.run(debug=True)