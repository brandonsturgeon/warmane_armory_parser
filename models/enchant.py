from typing import Optional
from models.jsonifiable import JSONifiable


class Enchant(JSONifiable):
    def __init__(self,
                 enchant_id: Optional[str] = None,
                 effect: Optional[str] = None):

        self.id = enchant_id
        self.effect = effect
