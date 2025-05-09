from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['GET'])
def calculate():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        op = request.args.get('op')

        if op == 'add':
            result = num1 + num2
        elif op == 'subtract':
            result = num1 - num2
        elif op == 'multiply':
            result = num1 * num2
        elif op == 'divide':
            if num2 == 0:
                return jsonify({'error': 'Division by zero'}), 400
            result = num1 / num2
        else:
            return jsonify({'error': 'Invalid operation'}), 400

        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=444)
