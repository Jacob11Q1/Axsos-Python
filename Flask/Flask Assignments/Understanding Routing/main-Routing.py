# Undrstanding Routing Assignment:

from flask import Flask
app = Flask(__name__)

# 1) Root Rout:
@app.route('/')
def hello_world():
    return "Hello World!"

# 2) Champion Route:
@app.route('/Champion')
def champion():
    return "Champion!"

# 3) Say Name Route:
@app.route('/say/<name>')
def say_hi(name):
    return f"Hi {name.capitalize()}!"

# 4) Repeat Route:
@app.route('/repeat/<int:num>/<word>')
def report_word(num , word):
    num = int(num)
    output = ""
    for i in range(num):
        output += word + "<br>"
    return output

# Sensi Bonus Error:
@app.errorhandler(404)
def page_error(x):
    return "Sorry! No response. Try again." , 404

if __name__ == "__main__":
    app.run(debug=True)