from mongoengine import Document, StringField, IntField, DateTimeField
import datetime

class FoodType(Document):
    name = StringField()

class FoodItem(Document):
    item_name = StringField()
    food_id = StringField()

class DuckPark(Document):
    item_id = StringField(required=True)
    name = StringField()
    count = IntField(required = True, min_value = 0, default = 1)
    at = DateTimeField(required=True, default=datetime.datetime.now())
    lat = IntField(required = True, min_value = -90, max_value = 90)
    lng = IntField(required = True, min_value = -180, max_value = 180)
