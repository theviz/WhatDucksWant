# ASSUMPTIONS:
# ID, TITLE, CONTENT are considered as mandatory fields.
# The patterns are derived from the model input.
# Patterns:
#   id => Start with a character and followed by characters or numbers
#   type => characters, numbers, hyphens, underbars, and space.
#   description => characters, special characters, and space.
#   Views and timestamp should be greater than 0
class Schema:
    def __init__(self):
        self.food_type = {
            "type": "object",
            "properties": {
                "foodname": {
                    "type": "string",
                    "minLength": 2,
                    "pattern": "^[A-Za-z][A-Za-z0-9-_]*$"
                }
            },
            "required": ["foodname"]
        }
        self.food_item = {
            "type" : "object",
            "properties": {
                "itemname": {
                    "type": "string",
                    "minLength": 2,
                    "pattern": "^[A-Za-z][A-Za-z0-9-_]*$"
                },
                "food_id": {
                    "type": "string",
                    "minLength": 2,
                    "pattern": "^[A-Za-z0-9-_]*$"
                }
            },
            "required": ["itemname", "food_id"]
        }
        self.duck_food = {
            "type": "object",
            "properties": {
                "item_id": {
                    "type": "string",
                    "minLength": 2,
                    "pattern": "^[A-Za-z0-9-_]*$"
                },
                "name": {
                    "type": "string",
                    "minLength": 2,
                    "pattern": "^[A-Za-z0-9-_\s]*$"
                },
                "count": {
                    "type": "number",
                    "minimum": 0
                },
                "at": {
                    "type": "number",
                    "minimum": 0,
                },
                "lat": {
                    "type": "number",
                    "minimum": -90,
                    "maximum": 90
                },
                "lng": {
                    "type": "number",
                    "minimum": -180,
                    "maximum": 180
                },
            },
            "required": ["item_id", "count", "lat", "lng"]
        }
