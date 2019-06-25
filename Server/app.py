from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "OK"


@app.route('/GetShoppingList', methods=['POST'])
def get_shopping_list():
    return "Shopping list"

if __name__ == "__main__":
    app.run(port=5000)