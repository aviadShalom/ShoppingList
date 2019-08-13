from DB.DBUtils import DB
from conf import config
import json

shopping_list_create_script = """create table if not exists shopping_list (
                                    id integer primary key AUTOINCREMENT,
                                    name text,
                                    created text);"""

shopping_list_items_create_script = """create table if not exists shopping_list_items (
                                        id integer primary key AUTOINCREMENT,
                                        list_id integer not null,
                                        item_id integer not null,
                                        quantity integer not null,
                                        created text
                                        );
                                        """

shopping_items_table_create_script = """create table if not exists shopping_items (
                                            item_id integer primary key AUTOINCREMENT,
                                            item_name text not null,
                                            img_link text
                                            ); """


def setup_process():
    print "Start Setup..."
    db = DB(config.DB_PATH)
    print "Create Shopping List Table"
    db.execute(shopping_list_create_script)

    print "Create Shopping List items Table"
    db.execute(shopping_list_items_create_script)

    print "Create Shopping items Table"
    db.execute(shopping_items_table_create_script)

    list_tables(db)
    build_demo_data(db)


def list_tables(db):
    query = "SELECT name FROM sqlite_master WHERE type='table';"
    data = db.query(query)
    print data


def build_demo_data(db):

    with open('conf/init_data.json') as json_file:
        data = json.load(json_file)

    insert_shopping_items(db, data['items'])

    insert_shopping_list_items(db, data['shopping_list_demo'])
    # db.insert_data(db.SHOPPING_LIST_TABLE, data['shopping_list_demo'])
    # db.insert_data(db.ITEMS_TABLE, data['items'])


def insert_shopping_items(db, item_list):

    for item in item_list:
        ret_val = db.insert_new_item(data=item)
        if ret_val < 1:
            print "Failed to insert row: " + item


def insert_shopping_list_items(db, shopping_list):

    for item in shopping_list:
        ret_val = db.insert_new_shopping_list_item(data=item)
        if ret_val < 1:
            print "Failed to insert row: " + item


def test():
    # sql = "update shopping_items set img_link = 'tomato.jpg' where item_id = 3"
    # db = DB(config.DB_PATH)
    # data = 'eggs.jpg'
    # db.execute(sql)
    sql = "select id, list_id, quantity, created, item_name, img_link " \
          "from shopping_list_items join shopping_items on shopping_list_items.item_id = shopping_items.item_id "

    db = DB(config.DB_PATH)
    result = db.query(sql)

    print result


if __name__ == "__main__":
    # setup_process()
    test()