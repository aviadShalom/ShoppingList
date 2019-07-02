from tinydb import TinyDB, Query,where


class DB:

    def __init__(self,db_path):
        self.__db = TinyDB(db_path)
        self.SHOPPING_LIST_TABLE = "ShoppingList"
        self.ITEMS_TABLE = "ShoppingItems"

    def create_table(self, table_name,override):
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

    def insert_data(self,table_name, data):
        table = self.__db.table(table_name)
        table.insert_multiple(data)

    def get_shopping_list(self):
        table = self.__db.table(self.SHOPPING_LIST_TABLE)
        return table.all()

    def get_items_list(self):
        table = self.__db.table(self.ITEMS_TABLE)
        return table.all()

    def get_shopping_list_item(self,item_id):
        table = self.__db.table(self.SHOPPING_LIST_TABLE)

        ret_val = table.search(where('id') == int(item_id))
        return ret_val
