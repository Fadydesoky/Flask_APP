from email import message
from flask import  request
import uuid
from db import ItemDatabase
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import ItemGetSchema, ItemOptionalQuerySchema, ItemQuerySchema, ItemSchema, SuccessMessageSchema

blp = Blueprint("Items", __name__, description="Operations on items")


@blp.route("/item")
class Item(MethodView):

    def __init__(self):
        self.db = ItemDatabase()

    @blp.response(200, ItemGetSchema(many=True))
    @blp.arguments(ItemOptionalQuerySchema, location="query")
    def get(self, args):
        id = args.get('id')  
        if id is None:
            return self.db.get_items()
        else:
            result = self.db.get_item(id)
            if result is None:
                abort(404, message="Record doesn't exist")
            return result

    @blp.arguments(ItemSchema) 
    @blp.response(200, SuccessMessageSchema)
    @blp.arguments(ItemQuerySchema, location="query")
    def put(self, request_data, args):
        id = args.get('id')
        if self.db.update_item(id, request_data):
            return {'message': "Item updated successfully"}
        abort(404, message="Item not found")

    @blp.arguments(ItemSchema)
    @blp.response(200, SuccessMessageSchema)
    def post(self, request_data):
        id  = uuid.uuid4().hex
        self.db.add_item(id, request_data)
        return {"message": "Item added succesfully"}, 201

    @blp.response(200, SuccessMessageSchema)
    @blp.arguments(ItemQuerySchema, location="query")
    def delete(self, args):
        id = args.get('id')
        if self.db.delete_item(id):
            return {'message': 'Item deleted'}   
        abort(404, message="Given id doesn't exist.")