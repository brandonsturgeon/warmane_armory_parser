from typing import Literal
from models.item import Item
from models.jsonifiable import JSONifiable

ITEM_SLOTS = Literal[
    "head", "neck", "shoulder", "back", "chest", "shirt",
    "tabard", "wrist", "hands", "waist", "legs", "feet",
    "ring1", "ring2", "trinket1", "trinket2", "main-hand",
    "off-hand", "relic"
]


class EquippedItems(JSONifiable):
    def set_slot(self, slot: ITEM_SLOTS, item: Item):
        setattr(self, slot, item)
