from flask import Flask, request
from connection import Connection
from config import Config
from schema import Schema
from handler import Handler
from models import *
from mongoengine import connect
from datetime import datetime
from flask_expects_json import expects_json
import json
import urllib

schema = Schema()
config = Config()

app = Flask(__name__)
connect('parks', host='mongodb://superuser:freshworks@mongo:27017/parks?authSource=admin')

@app.route('/')
def hello_world():
    author = FoodType(name=request.args.get('name', ''))
    author.save()
    return 'Hello, Docker!' + config.MONGO_URL[0]

@app.route('/food-type', methods=["POST"])
@expects_json(schema.food_type)
def save_food_type():
    body = request.json
    try:
        type = FoodType(name=body['foodname'])
        result = type.save()
        return {'id' : str(result.id)}, 201

    except Exception as e:
        print(e, flush = True)
        return {'error' : str(e)}, 500

@app.route('/food-type', methods=["GET"])
def get_food_type():
    return FoodType.objects().to_json()

@app.route('/food-item', methods=["POST"])
@expects_json(schema.food_item)
def save_food_item():
    body = request.json
    try:
        item_name = body['itemname']
        food_id = body['food_id']

        item = FoodItem(
            item_name = item_name,
            food_id = food_id
        )

        result = item.save()
        return {'id' : str(result.id)}, 201

    except Exception as e:
        print(e, flush = True)
        return {'error' : str(e)}, 500

@app.route('/food-item', methods=["GET"])
def get_food_item():
    return FoodItem.objects().to_json()

@app.route('/duck-food', methods=["POST"])
@expects_json(schema.duck_food)
def save_duck_feed():
        body = request.json

        item_id = body['item_id']
        name = body['name']
        count = body['count']
        at = body['at']
        date = None
        if at != None:
            date =  datetime.fromtimestamp(int(at))
        lat = body['lat']
        lng = body['lng']


        park = DuckPark(
            item_id = item_id,
            name = name,
            count = count,
            at = date,
            lat = lat,
            lng = lng
        )

        result = park.save()
        return {'id' : str(result.id)}, 201
