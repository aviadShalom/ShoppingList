from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "OK"


@app.route('/GetShoppingList', methods=['POST'])
def get_shopping_list():
    return jsonify({'app':'sssss'})

if __name__ == "__main__":
    app.run(port=5000)