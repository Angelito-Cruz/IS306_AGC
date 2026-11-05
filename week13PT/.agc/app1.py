from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get('/')
def home():
    return jsonify({"message": "Welcome to the Flask API!"})

@app.post('/api/greet')
def greet():
    data = request.get_json(silent=True) or {}
    name = str(data.get("name", "")).strip()

    if not name:
        return jsonify({"error": "Name is required."}), 400

    return jsonify({"message": f"Hello, {name}!"})

if __name__ == '__main__':
    app.run(debug=True)