from models.jsonifiable import JSONifiable
from typing import Dict


class Gem(JSONifiable):
    def __init__(self,
                 name: str,
                 colors: Dict[str, bool],
                 effect: str,
                 enchant_id: str):

        self.name = name
        self.colors = colors
        self.effect = effect
        self.enchant_id = enchant_id
