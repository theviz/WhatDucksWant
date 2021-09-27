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
        return {'id' : str(result.id)}

    def handle_exception(self, exception):
        print(exception, flush = True)
        return {'error' : str(exception)}

    def create_food_type(self, data):
        try:
            foodtype = FoodType(name = data['food_type'])
            result = foodtype.save()
            return self.handle_result(result)
        except Exception as e:
            print(e)
            raise ValueError('Error while creating food type')

    def get_food_type(self, foodtype):
        return FoodType.objects(name = foodtype).to_json()

    def get_food_types(self):
        return FoodType.objects().to_json()

    def create_food_item(self, data):
        try:
            item = FoodItem(
                item_name = data['item_name'],
                food_id = data['food_id']
            )
            result = item.save()
            return self.handle_result(result)
        except Exception as e:
            print(e)
            raise ValueError('Error while creating food item')

    def get_food_item(self, itemname):
        return FoodItem.objects(item_name = itemname).to_json()

    def get_food_items(self):
        return FoodItem.objects().to_json()

    def get_first_id(self, data):
        return data[0]['_id']['$oid']

    def get_item_id_for_data(self, data):
        food_item = json.loads(self.get_food_item(data['item_name']))
        item_id = None

        if len(food_item) != 0:
            item_id = self.get_first_id(food_item)
        else:
            food_type = json.loads(self.get_food_type(data['food_type']))
            type_id = None
            if len(food_type) != 0:
                type_id = self.get_first_id(food_type)
            else:
                type_id = self.create_food_type(data)['id']
            data['food_id'] = type_id
            item_id = self.create_food_item(data)['id']
        return item_id

    def create_duck_food(self, data):
        try:
            at = data['at']
            date = None
            if at != None:
                date =  dt.fromtimestamp(int(at))
            item_id = self.get_item_id_for_data(data)
            print(item_id)
            park = DuckPark(
                item_id = item_id,
                name = data['name'],
                count = data['count'],
                at = date,
                location = data['location'],
                food_amount = data['food_amount']
            )
            result = park.save()
            return self.handle_result(result)

        except Exception as e:
            print(e)
            raise ValueError('Error while saving duck food')
