from decimal import Decimal
from datetime import datetime, date, time
import json


class BaseModel:
    def to_json(self):
        json_data = {}

        for name, value in vars(self).items():
            if type(value) in (Decimal, datetime, date, time):
                json_data[name] = str(value)
            else:
                json_data[name] = value
        
        return json_data


    @classmethod
    def from_json(cls, json_data):
        return cls(**json_data)


    def __str__(self):
        return json.dumps(self.to_json(), ensure_ascii=False, indent=4)