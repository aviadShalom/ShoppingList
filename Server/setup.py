from DB.DBUtils import DB
from conf import config
import json


def setup_process():
    print "Start Setup..."
    db = DB(config.DB_PATH)
    print "Create Table"
    print db.create_table(db.SHOPPING_LIST_TABLE, True)
    print db.create_table(db.ITEMS_TABLE, True)

    print db.get_tables_list()
    build_demo_data(db)


def build_demo_data(db):

    with open('conf/init_data.json') as json_file:
        data = json.load(json_file)

    db.insert_data(db.SHOPPING_LIST_TABLE, data['shopping_list_demo'])
    db.insert_data(db.ITEMS_TABLE, data['items'])


if __name__ == "__main__":
    setup_process()