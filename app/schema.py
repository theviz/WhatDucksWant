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
        self.duck_feed = {
            "type": "object",
            "properties": {
                "food_type": {
                    "type": "string",
                    "minLength": 2,
                    "pattern": "^[A-Za-z0-9-_]*$"
                },
                "item_name": {
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
                "quantity": {
                    "type": "number",
                    "minimum": 0,
                },
                "location": {
                    "type": "string",
                    "minLength": 2,
                    "pattern": "^[A-Za-z0-9-_\s]*$"
                },
            },
            "required": ["at", "count", "location", "food_type", "item_name"]
        }
