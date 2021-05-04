import bs4
from bs4 import BeautifulSoup
from typing import Sequence, Union
from models.item import Item
from models.equipped_items import EquippedItems, ITEM_SLOTS
from parser.armory import ArmoryParser
from parser.item.item import ItemParser

ITEM_ORDER: Sequence[ITEM_SLOTS] = [
    "head", "neck", "shoulder", "back", "chest", "shirt",
    "tabard", "wrist", "hands", "waist", "legs", "feet",
    "ring1", "ring2", "trinket1", "trinket2", "main-hand",
    "off-hand", "relic"
]


class ItemsParser(ArmoryParser):
    def get_section(self, soup: BeautifulSoup) -> BeautifulSoup:
        return soup.find(class_="item-model")

    def parse(self) -> EquippedItems:
        item_set = EquippedItems()
        items: bs4.element.ResultSet = self.page.find_all(class_="item-slot")

        for i in range(len(ITEM_ORDER)):
            slot: ITEM_SLOTS = ITEM_ORDER[i]
            item: Union[Item, None] = ItemParser(items[i]).parse()

            if item:
                item_set.set_slot(slot, item)

        return item_set
