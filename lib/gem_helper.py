import json
from typing import Dict, Type, Union
from models.gem import Gem

LOOKUP = {}

with open("lib/data/gem_data.json", "rb") as all_gem_data:
    LOOKUP = json.loads(all_gem_data.read())

LOOKUP_BY_ENCHANT_ID = {v["enchant_id"]: v for _, v in LOOKUP.items()}
GEM_DATA_TYPE: Type = Dict[str, Union[Dict, str]]


class GemHelper:
    def __init__(self):
        self.lookup: Dict[str, Dict] = LOOKUP
        self.lookup_by_enchant_id: Dict[str, Dict] = LOOKUP_BY_ENCHANT_ID

    def make_gem_from_data(self, data: GEM_DATA_TYPE) -> Gem:
        return Gem(
            name=data["name"],
            colors=data["colors"],
            effect=data["effect"],
            enchant_id=data["enchant_id"]
        )

    def get(self, gem_id: str) -> Gem:
        gem_data: GEM_DATA_TYPE = self.lookup.get(gem_id)
        return self.make_gem_from_data(gem_data)

    def get_by_enchant_id(self, enchant_id: str) -> Gem:
        gem_data: GEM_DATA_TYPE = self.lookup_by_enchant_id.get(enchant_id)
        return self.make_gem_from_data(gem_data)
