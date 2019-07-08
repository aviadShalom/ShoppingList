from tinydb import TinyDB, Query, where
import logging
import sqlite3
import json

logger = logging.getLogger("Log")


class DB:

    def __init__(self, db_path):
        self.__conn = sqlite3.connect(db_path, check_same_thread=False)
        self.__conn.row_factory = self.dict_factory

        self.__db = None

        self.SHOPPING_LIST_TABLE = "ShoppingList"
        self.ITEMS_TABLE = "ShoppingItems"

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def execute(self, query):
        try:
            cur = self.__conn.cursor()
            cur.execute(query)
            cur.close()
            return True
        except Exception as e:
            logger.error(e.message)
            return False

    def query(self, query, query_params=None):
        try:
            cur = self.__conn.cursor()
            if query_params:
                cur.execute(query, query_params)
            else:
                cur.execute(query)
            result = cur.fetchall()
            cur.close()
            return result
        except Exception as e:
            logger.error(e.message)
            return None

    def insert_new_shopping_list_item(self, data):
        try:
            sql = "select * from shopping_list;"
            query = "insert into shopping_list (name, created) values (?, ?);"
            if data is None:
                return 0

            cur = self.__conn.cursor()
            cur.execute(query, (data['name'], data['created']))

            ret_id = cur.lastrowid
            self.__conn.commit()
            cur.execute(sql)
            test = cur.fetchall()
            print test
            cur.close()

            return ret_id

        except Exception as e:
            logger.error(e.message)
            return -1

    def insert_new_item(self, data):
        try:

            sql = "select * from shopping_items;"
            query = "insert into shopping_items (item_name, img_link) values (?, ?);"
            if data is None:
                return 0

            cur = self.__conn.cursor()
            cur.execute(query, (data['item_name'], data['img_link']))

            ret_id = cur.lastrowid
            self.__conn.commit()
            cur.execute(sql)
            test = cur.fetchall()
            print test
            cur.close()

            return ret_id

        except Exception as e:
            logger.error(e.message)
            return -1

    def json_serializer(self, c):
        try:
            columns = []
            result = []
            for column in c.description:
                columns.append(column[0])
            for row in c.fetchall():
                temp_row = dict()
                for key, value in zip(columns, row):
                    temp_row[key] = value
                    result.append(temp_row)
            return result
        except:
            raise Exception('Invalid cursor provided')

    def create_table(self, table_name, override):
        tables = self.get_tables_list()
        if table_name in tables:
            if override:
                self.__db.purge_table(table_name)
            else:
                return 'Table is already created'

        self.__db.table(table_name)
        return 1

    def get_tables_list(self):
        return self.__db.tables()

    def insert_shopping_list(self, data):
        table = self.__db.table(self.SHOPPING_LIST_TABLE)
        table.insert_multiple(data)

    def insert_data(self, table_name, data):
        table = self.__db.table(table_name)
        table.insert_multiple(data)

    def get_shopping_list(self):

        try:
            query = "select id,name,created from shopping_list;"

            ret_val = self.query(query, None)

            return ret_val
        except Exception as e:
            logger.error(e.message)
            raise NameError("Failed to get Data")

    def get_items_list(self):
        try:
            sql = "select item_id, item_name, img_link from shopping_items;"
            result = self.query(sql)
            return result
        except Exception as e:
            logger.error(e.message)
            raise NameError("Failed to get Data")

    def get_shopping_list_item(self, item_id):
        try:
            sql = "select id, name, created from shopping_list where id = ?;"

            result = self.query(sql,item_id)

            return result
        except Exception as e:
            logger.error(e.message)
            raise NameError("Failed to get Data")
