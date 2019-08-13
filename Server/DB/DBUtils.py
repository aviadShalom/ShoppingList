from tinydb import TinyDB, Query, where
import logging
import sqlite3
from datetime import date

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

    def execute_with_id(self, query, sql_params=None):
        try:
            cur = self.__conn.cursor()
            if sql_params:
                cur.execute(query, sql_params)
            else:
                cur.execute(query)
            self.__conn.commit()
            ret_val = cur.lastrowid
            cur.close()
            return ret_val
        except Exception as e:
            logger.error(e.message)
            raise NameError("Failed to execute query {0}".format(query))

    def execute(self, query, sql_params=None):
        try:
            cur = self.__conn.cursor()
            if sql_params:
                cur.execute(query, sql_params)
            else:
                cur.execute(query)
            self.__conn.commit()
            cur.close()
            return True
        except Exception as e:
            logger.error(e.message)
            raise NameError("Failed to execute query {0}".format(query))

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

    def update_shopping_list_name(self, item_id, name):
        try:
            sql = "update shopping_list set name = ? where id = ?"

            return self.execute(sql,(name, item_id))

        except Exception as e:
            logger.error(e.message)
            raise NameError("Failed to Update Name")

    def create_shopping_list(self, name):
        try:
            sql="insert into shopping_list (name, created) values(?,?)"
            current_date = date.today().strftime("%d/%m/%Y")
            ret_val = self.execute_with_id(sql,(name, current_date))

            return ret_val

        except Exception as e:
            logger.error(e.message)
            raise NameError("Failed to create shopping list")

    def delete_shopping_list(self, item_id):
        try:
            sql = "delete from shopping_list_items where list_id = ?"
            ret_val = self.execute(sql, item_id)
            if ret_val:
                sql = "delete from shopping_list where id = ?"
                return self.execute(sql, item_id)
            else:
                return False

        except Exception as e:
            logger.error(e.message)
            raise NameError("Failed to delete Shopping List")

    def add_shopping_item_to_list(self,list_id, item_id, quantity):
        try:
            sql = "insert into shopping_list_items(list_id, item_id, quantity, created) " \
                  " values (?,?,?,?)"
            current_date = date.today().strftime("%d/%m/%Y")
            ret_val = self.execute(sql, (list_id, item_id, quantity, current_date))

            return ret_val

        except Exception as e:
            logger.error(e.message)
            raise NameError("Failed to add item {0} to list {1}".format(item_id, list_id))

    def get_shopping_list_items(self, list_id):
        try:
            sql = "select id, list_id, quantity, created, item_name, img_link " \
                  "from shopping_list_items join shopping_items on shopping_list_items.item_id = " \
                  " shopping_items.item_id where list_id = ?"

            result = self.query(sql, list_id)

            return result
        except Exception as e:
            logger.error(e.message)
            raise NameError("Failed to get Shopping list items")

    def delete_item_from_list(self, list_id, item_id):
        try:
            sql = "delete from shopping_list_items where list_id = ? and id = ?"
            return self.execute(sql, (list_id, item_id))

        except Exception as e:
            logger.error(e.message)
            raise NameError("Failed to Delete item from List")

