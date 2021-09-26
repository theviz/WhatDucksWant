import json
from datetime import datetime as dt
from config import Config
from models import *
from collections import namedtuple
from types import SimpleNamespace

class Util:
    def __init__(self):
        self.config = Config()

    def handle_result(self, result):
        return {'id' : str(result.id)}, self.config.HTTP_CREATED

    def handle_exception(self, exception):
        print(exception, flush = True)
        return {'error' : str(exception)}, self.config.SERVER_ERROR

    def create_food_type(self, data):
        try:
            foodtype = FoodType(name = data['foodname'])
            result = foodtype.save()
            return self.handle_result(result)
        except Exception as e:
            print(e)
            raise ValueError('Error while creating food type')

    def get_food_types(self):
        return FoodType.objects().to_json(), self.config.HTTP_CREATED

    def create_food_item(self, data):
        try:
            item = FoodItem(
                item_name = data['itemname'],
                food_id = data['food_id']
            )
            result = item.save()
            return self.handle_result(result)
        except Exception as e:
            print(e)
            raise ValueError('Error while creating food item')

    def get_food_items(self):
        return FoodItem.objects().to_json(), self.config.HTTP_CREATED

    def create_duck_food(self, data):
        try:
            at = data['at']
            date = None
            if at != None:
                date =  dt.fromtimestamp(int(at))

            park = DuckPark(
                item_id = data['item_id'],
                name = data['name'],
                count = data['count'],
                at = date,
                lat = data['lat'],
                lng = data['lng']
            )

            result = park.save()
            return self.handle_result(result)

        except Exception as e:
            print(e)
            raise ValueError('Error while saving duck food')
