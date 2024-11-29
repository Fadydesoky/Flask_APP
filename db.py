import pyodbc
from flask import Flask, render_template  # تأكد من استيراد render_template هنا

class ItemDatabase:
    def __init__(self):
        self.conn = pyodbc.connect('DRIVER={SQL Server};'
                                    'SERVER=DESKTOP-KI9AI6G\SQLEXPRESS;'
                                    'DATABASE=Cafe;'
                                    'Trusted_Connection=yes;')       
        self.cursor = self.conn.cursor()

    def get_items(self):
        result = []
        query = "SELECT * FROM item"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            item_dict = {}
            item_dict["id"], item_dict["name"], item_dict["price"] = row
            result.append(item_dict)
        return result

    def get_item(self, item_id):
        query = f"select * from item where id = '{item_id}'"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            item_dict = {}
            item_dict["id"], item_dict["name"], item_dict["price"] = row
            return [item_dict]

    def add_item(self, id, body):
        query = f"insert into item(id, name, price) values ('{id}', '{body['name']}', {body['price']})"
        self.cursor.execute(query)
        self.conn.commit()

    def update_item(self, id, body):
        query = f"UPDATE item SET name = '{body['name']}', price = {body['price']} where id = '{id}'"
        self.cursor.execute(query)
        if self.cursor.rowcount == 0:
            return False
        else:
            self.conn.commit()
            return True

    def delete_item(self, id):
        query = f"delete from item where id = '{id}'"
        self.cursor.execute(query)
        if self.cursor.rowcount == 0:
            return False
        else:
            self.conn.commit()
            return True