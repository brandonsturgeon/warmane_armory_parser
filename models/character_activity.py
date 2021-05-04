from models.jsonifiable import JSONifiable


class CharacterActivity(JSONifiable):
    def __init__(self, name: str, when: str):
        self.name = name
        self.when = when
