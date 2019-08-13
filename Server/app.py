from flask import Flask, request, jsonify
from flask_cors import CORS
from DB.DBUtils import DB
from conf import config
import logging


app = Flask(__name__)
CORS(app)
db = DB(config.DB_PATH)

logger = logging.getLogger("Log")
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('Log.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


@app.route('/')
def home():
    return "OK"


@app.route('/GetShoppingList', methods=['POST'])
def get_shopping_list():
    data = db.get_shopping_list()
    return jsonify(data)


@app.route('/GetItemsList', methods=['POST'])
def get_items_list():
    try:
        data = db.get_items_list()
        return jsonify(data)
    except Exception as e:
        logger.error(e)
        return "-1"


@app.route('/GetShoppingListItem/<item_id>', methods=['POST'])
def get_shopping_list_item(item_id):

    try:
        item = db.get_shopping_list_item(item_id)
        if len(item) > 0:
            return jsonify(item)
        else:
            return "0"
    except Exception as e:
        logger.error(e.message)
        return "-1"


@app.route('/UpdateShoppingListName/<item_id>/<name>', methods=['POST'])
def update_shopping_list_name(item_id, name):
    try:
        if db.update_shopping_list_name(item_id, name):
            return "1"
        else:
            return "0"
    except Exception as e:
        logger.error(e.message)
        return "-1"


@app.route('/CreateNewShoppingList/<name>', methods=['POST'])
def create_new_shopping_list(name):
    try:
        ret_val =  db.create_shopping_list(name)
        return str(ret_val)

    except Exception as e:
        logger.error(e.message)
        return "-1"


@app.route('/DeleteShoppingList/<item_id>', methods=['POST'])
def delete_shopping_list(item_id):
    try:
        ret_val = db.delete_shopping_list(item_id)
        if ret_val:
            return "1"
        else:
            return "0"

    except Exception as e:
        logger.error(e.message)
        return "-1"


@app.route('/AddItemToList/<list_id>/<item_id>/<quantity>', methods=['POST'])
def add_item_to_list(list_id, item_id, quantity):
    try:
        print list_id
        print item_id
        print quantity
        result = db.add_shopping_item_to_list(list_id, item_id, quantity)
        if result:
            return "1"
        else:
            return "0"

    except Exception as e:
        logger.error(e.message)
        return "-1"


@app.route('/GetShoppingListItems/<list_id>',  methods=['POST'])
def get_shopping_list_items(list_id):
    try:
        result = db.get_shopping_list_items(list_id)

        return jsonify(result)

    except Exception as e:
        logger.error(e.message)
        return "-1"


@app.route('/DeleteItemFromList/<list_id>/<item_id>', methods=['POST'])
def delete_item_from_list(list_id, item_id):
    try:
        if db.delete_item_from_list(list_id, item_id):
            return "1"
        else:
            return "0"

    except Exception as e:
        logger.error(e.message)
        return "-1"

if __name__ == "__main__":
    logger.info("App Start")
    app.run(port=5000)
