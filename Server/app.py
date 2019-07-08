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
            return jsonify(item[0])
        else:
            return "0"
    except Exception as e:
        logger.error(e.message)
        return "-1"




if __name__ == "__main__":
    logger.info("App Start")
    app.run(port=5000)
