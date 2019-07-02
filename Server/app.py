from flask import Flask, request, jsonify
from flask_cors import CORS
from DB.DBUtils import DB
from conf import config

app = Flask(__name__)
CORS(app)
db = DB(config.DB_PATH)


@app.route('/')
def home():
    return "OK"


@app.route('/GetShoppingList', methods=['POST'])
def get_shopping_list():
    data = db.get_shopping_list()
    return jsonify(data)


@app.route('/GetItemsList', methods=['POST'])
def get_items_list():
    data = db.get_items_list()
    return jsonify(data)


@app.route('/GetShoppingListItem/<item_id>', methods=['POST'])
def get_shopping_list_item(item_id):
    print item_id
    item = db.get_shopping_list_item(item_id)
    return jsonify(item)


if __name__ == "__main__":
    app.run(port=5000)
