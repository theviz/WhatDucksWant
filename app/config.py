import os
import urllib

class Config:
    def __init__(self):
        self.MONGO_URL = 'mongodb+srv://superuser:' + urllib.parse.quote_plus('gm90D9XndaBLLsM8') + '@cluster0.paipk.mongodb.net/parks?retryWrites=true&w=majority',
        self.PARKS_COLLECTION = 'parks',
        self.FOOD_TABLE='food'
        self.FOOD_TYPE_TABLE='food_type'
        self.DUCK_FOOD='duck_food'
        self.HTTP_CREATED = 201
        self.SERVER_ERROR = 500
        self.ROLLBAR_ACCESS_TOKEN = 'f9d300f264d94aa3acfb24408e6545ef'
