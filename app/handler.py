import json
from util import Util
from config import Config
from models import *
from collections import namedtuple
from types import SimpleNamespace

class Handler:
    def __init__(self):
        self.util = Util()
        self.config = Config()

    def POST_Food_Type(self, data):
        try:
            return self.util.create_food_type(data), self.config.HTTP_CREATED
        except Exception as e:
            return self.util.handle_exception(e), self.config.SERVER_ERROR

    def GET_Food_Type(self):
        try:
            return self.util.get_food_types(), self.config.HTTP_SUCCESS
        except Exception as e:
            return self.util.handle_exception(e), self.config.SERVER_ERROR

    def POST_Food_Item(self, data):
        try:
            return self.util.create_food_item(data), self.config.HTTP_CREATED
        except Exception as e:
            return self.util.handle_exception(e)

    def GET_Food_Item(self):
        try:
            return self.util.get_food_items(), self.config.HTTP_SUCCESS
        except Exception as e:
            return self.util.handle_exception(e), self.config.SERVER_ERROR

    def POST_Duck_Food(self, data):
        try:
            return self.util.create_duck_food(data), self.config.HTTP_CREATED
        except Exception as e:
            return self.util.handle_exception(e), self.config.SERVER_ERROR

    def GET_Duck_Food(self):
        try:
            return self.util.get_duck_food(), self.config.HTTP_SUCCESS
        except Exception as e:
            return self.util.handle_exception(e), self.config.SERVER_ERROR
