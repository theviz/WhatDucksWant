import os
class Config:
    def __init__(self):
        self.MONGO_URL = os.getenv('MONGO_URL'),
        self.PARKS_COLLECTION = 'parks',
        self.FOOD_TABLE='food'
        self.FOOD_TYPE_TABLE='food_type'
        self.DUCK_FOOD='duck_food'
        self.HTTP_CREATED = 201
        self.SERVER_ERROR = 500
        self.ROLLBAR_ACCESS_TOKEN = os.getenv('ROLLBAR_ACCESS_TOKEN')
