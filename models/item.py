from typing import Literal, Optional
from models.jsonifiable import JSONifiable
from models.item_gems import ItemGems
from models.enchant import Enchant
SOCKET_NUMBERS = Literal[1, 2, 3]


class Item(JSONifiable):
    def __init__(self,
                 item_id: str,
                 gems: ItemGems,
                 enchant: Optional[Enchant] = None):

        self.item_id = item_id
        self.enchant = enchant
        self.gems = gems
