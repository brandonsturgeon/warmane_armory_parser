from bs4 import BeautifulSoup
from typing import Dict, Optional, Sequence, Union
from parser.armory import ArmoryParser
from models.item_gems import ItemGems
from models.item import Item
from models.gem import Gem
from models.enchant import Enchant
from lib.gem_helper import GemHelper
from lib.enchant_ids import EnchantIDs


enchant_ids = EnchantIDs()
gem_helper = GemHelper()
GEM_INFO_TYPE = Dict[str, Union[bool, Gem]]


class ItemParser(ArmoryParser):
    def get_section(self, soup: BeautifulSoup) -> BeautifulSoup:
        return soup.a

    def parse_gems_info(self, gems_line: Optional[str] = None) -> ItemGems:
        if not gems_line:
            return ItemGems()

        gems_info: Dict[str, Gem] = {}
        gems: list = gems_line.split(":")

        for i, gem_enchant_id in enumerate(gems):
            i: int = i + 1
            socket_key: str = f"socket{i}"

            if gem_enchant_id == "0":
                continue

            gem_item_info: Gem = gem_helper.get_by_enchant_id(gem_enchant_id)
            gems_info[socket_key] = gem_item_info

        return ItemGems(**gems_info)

    def parse_ench_info(self, enchant_id: Optional[str] = None) -> Enchant:
        if not enchant_id:
            return Enchant()

        return Enchant(
            enchant_id=enchant_id,
            effect=enchant_ids.get(enchant_id)
        )

    def parse(self) -> Union[Item, None]:
        # ['item=51543&ench=3842&gems=3642:3532:0']
        rel: Sequence[str] = self.page.get("rel", [])

        # Ignoring some garbage tags
        if len(rel) == 0:
            return

        # 'item=51543&ench=3842&gems=3642:3532:0'
        item_str: str = rel[0]

        # ['item=51543', 'ench=3842', 'gems=3642:3532:0']
        item_chunks: Sequence[str] = item_str.split("&")

        # [['item', '51543'], ['ench', '3842'], ['gems', '3642:3532:0']]
        parsed_chunks: Sequence[Sequence[str]] = [
            x.split("=") for x in item_chunks
        ]

        # {'item': '51543', 'ench': '3842', 'gems': '3642:3532:0'}
        item_data: Dict[str, str] = {i[0]: i[1] for i in parsed_chunks}

        gems: Union[str, None] = item_data.get("gems")
        gem_info: ItemGems = self.parse_gems_info(gems)

        ench = item_data.get("ench")
        enchant: Enchant = self.parse_ench_info(ench)

        return Item(
            item_id=item_data["item"],
            gems=gem_info,
            enchant=enchant
        )
