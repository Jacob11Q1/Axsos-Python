from flask import Flask, render_template

app = Flask(__name__)

# ============================
# Route: /lists — Pass lists to template
# ============================

@app.route('/lists')
def render_lists():
    student_info = [
        {'name' : 'Micheal' , 'age' : 35},
        {'name' : 'John' , 'age' : 30},
        {'name' : 'Mark' , 'age' : 25},
        {'name' : 'KB' , 'age' : 27}
    ]
    return render_template("lists.html" , random_numbers = [3,1,5] , students = student_info)

if __name__ == "__main__":
    app.run(debug=True)

# @app.route('/')
# def index():
#     """Render the index.html template with phrase and times variables."""
#     return render_template("index.html", phrase="hello", times=5)


# ============================
# Root Route: Render Home Page
# ============================
# @app.route('/')
# def hello_world():
#     """Render the index.html template"""
#     return render_template('index.html')

# def hello_world():
#     return 'Hellow World!'