from datetime import datetime
import json

class Url:
    id = None
    url = None
    created_date = None

    def __init__(self, url, id = None, created_date = datetime.now().strftime("%Y-%m-%d %X")):
        self.id = id
        self.url = url
        self.created_date = created_date


    def __str__(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.__str__()
