from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "some_secret_key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['loc'] = request.form['loc']
    session['lang'] = request.form['lang']
    session['comm'] = request.form['comm']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template(
        "show.html",
        name=session.get('name', ''),
        loc=session.get('loc', ''),
        lang=session.get('lang', ''),
        comm=session.get('comm', '')
    )

if __name__ == "__main__":
    app.run(debug=True)