from models.jsonifiable import JSONifiable


class Activity(JSONifiable):
    def __init__(self,
                 activity_id: str,
                 name: str,
                 when: str):

        self.id = activity_id
        self.name = name
        self.when = when
