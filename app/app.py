from flask import Flask, request, got_request_exception
import rollbar.contrib.flask
from handler import Handler
from config import Config
from schema import Schema
from mongoengine import connect
from flask_expects_json import expects_json
from flask_cors import CORS, cross_origin
import rollbar
import json
import os


handler = Handler()
config = Config()
schema = Schema()

app = Flask(__name__)
connect('parks', host= config.MONGO_URL)

CORS(app)

@app.before_first_request
def init_rollbar():
    rollbar.init(
        config.ROLLBAR_ACCESS_TOKEN,
        'production',
        root=os.path.dirname(os.path.realpath(__file__)),
        allow_logging_basic_config=False
    )

    got_request_exception.connect(rollbar.contrib.flask.report_exception, app)

@app.route('/')
def hello_world():
    return 'Welcome to What Ducks Want'

@app.route('/food-type', methods=["POST"])
@expects_json(schema.food_type)
def save_food_type():
    return handler.POST_Food_Type(request.json)

@app.route('/food-type', methods=["GET"])
def get_food_type():
    return handler.GET_Food_Type()

@app.route('/food-item', methods=["POST"])
@expects_json(schema.food_item)
def save_food_item():
    return handler.POST_Food_Item(request.json)

@app.route('/food-item', methods=["GET"])
def get_food_item():
    return handler.GET_Food_Item()

@app.route('/duck-food', methods=["POST"])
@expects_json(schema.duck_feed)
def save_duck_feed():
    return handler.POST_Duck_Food(request.json)

@app.route('/duck-food', methods=["GET"])
def export_duck_feed():
    return handler.GET_Duck_Food()


if __name__ == '__main__':
    from os import environ
    app.run(debug=False, host='0.0.0.0', port=environ.get("PORT", 5000))
