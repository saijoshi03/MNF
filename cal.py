from flask import Flask, request, jsonify

app = Flask(__name__)

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Cannot divide by zero"

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    operation = data.get("operation")
    x = data.get("x")
    y = data.get("y")

    if None in (operation, x, y):
        return jsonify({"error": "Missing data"}), 400

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        return jsonify({"error": "Inputs must be numbers"}), 400

    result = None
    if operation == "add":
        result = add(x, y)
    elif operation == "subtract":
        result = subtract(x, y)
    elif operation == "multiply":
        result = multiply(x, y)
    elif operation == "divide":
        result = divide(x, y)
    else:
        return jsonify({"error": "Invalid operation"}), 400

    return jsonify({"result": result})

@app.route("/")
def index():
    return "Calculator API is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
