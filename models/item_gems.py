from typing import Optional
from models.jsonifiable import JSONifiable
from models.gem import Gem


class ItemGems(JSONifiable):
    def __init__(self,
                 socket1: Optional[Gem] = None,
                 socket2: Optional[Gem] = None,
                 socket3: Optional[Gem] = None):

        self.socket1 = socket1
        self.socket2 = socket2
        self.socket3 = socket3
