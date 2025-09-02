from flask import Flask

app = Flask(__name__)

# ===============================
# Variable Rules Examples
# ===============================

@app.route('/success')
def success():
    """Simple success route"""
    return "Success"

@app.route('/hello/<name>')
def hello(name):
    """Greet a user by name"""
    print(f"Received name: {name}")
    return f"Hello, {name}"

@app.route('/users/<username>/<int:id>')
def show_user_profile(username, id):
    """Show a user profile with username and numeric ID"""
    print(f"Username: {username}")
    print(f"ID: {id}")
    return f"Username: {username}, ID: {id}"

# ===============================
# Run the Flask Application
# ===============================
if __name__ == "__main__":
    app.run(debug=True)