import json
from util import Util
from models import *
from collections import namedtuple
from types import SimpleNamespace

class Handler:
    def __init__(self):
        self.util = Util()

    def POST_Food_Type(self, data):
        try:
            return self.util.create_food_type(data)
        except Exception as e:
            return self.util.handle_exception(e)

    def GET_Food_Type(self):
        try:
            return self.util.get_food_types()
        except Exception as e:
            return self.util.handle_exception(e)

    def POST_Food_Item(self, data):
        try:
            return self.util.create_food_item(data)
        except Exception as e:
            return self.util.handle_exception(e)

    def GET_Food_Item(self):
        try:
            return self.util.get_food_items()
        except Exception as e:
            return self.util.handle_exception(e)

    def POST_Duck_Food(self, data):
        try:
            return self.util.create_duck_food(data)
        except Exception as e:
            return self.util.handle_exception(e)
