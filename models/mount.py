from models.jsonifiable import JSONifiable


class Mount(JSONifiable):
    def __init__(self, mount_id: str, name: str):
        self.id = mount_id
        self.name = name
