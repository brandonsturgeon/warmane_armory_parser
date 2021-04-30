from parser.armory import ArmoryParser
from parser.item.item import ItemParser


class ItemsParser(ArmoryParser):
    ITEM_ORDER = [
        "head", "neck", "shoulder", "back", "chest", "shirt",
        "tabard", "wrist", "hands", "waist", "legs", "feet",
        "ring1", "ring2", "trinket1", "trinket2", "main-hand",
        "off-hand", "relic"
    ]

    def get_section(self, soup):
        return soup.find(class_="item-model")

    def parse(self):
        item_data = {}
        items = self.page.find_all(class_="item-slot")

        for slot, item in zip(self.ITEM_ORDER, items):
            data = ItemParser(item).parse()
            item_data[slot] = data

        return item_data
