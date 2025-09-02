from flask import Flask, render_template, request

app = Flask(__name__)


fruits = [
    {"name": "Apple", "price": 1, "image": "apple.jpg"},
    {"name": "Banana", "price": 2, "image": "banana.jpg"},
    {"name": "Orange", "price": 3, "image": "orange.jpg"}
]

@app.route('/')
def index():
    return render_template('fruits.html', fruits=fruits)

@app.route('/checkout', methods=['POST'])
def checkout():
    customer_name = request.form.get('customer_name')
    total_fruits = 0
    total_cost = 0
    fruit_counts = {}

    
    for fruit in fruits:
        count = request.form.get(fruit['name'], '0')
        count = int(count) if count.isdigit() else 0
        fruit_counts[fruit['name']] = count
        total_fruits += count
        total_cost += count * fruit['price']

    print(f"Charging {customer_name} for {total_fruits} fruits.")

    return render_template('checkout.html', customer_name=customer_name, fruit_counts=fruit_counts, total_cost=total_cost)

if __name__ == "__main__":
    app.run(debug=True)