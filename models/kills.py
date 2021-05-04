from models.jsonifiable import JSONifiable


class KillsInfo(JSONifiable):
    def __init__(self, all_time: int, today: int):
        self.all_time = all_time
        self.today = today
