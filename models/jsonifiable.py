from json import dumps, JSONEncoder


class CustomEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class JSONifiable:
    def to_json(self) -> str:
        return dumps(self, cls=CustomEncoder)
