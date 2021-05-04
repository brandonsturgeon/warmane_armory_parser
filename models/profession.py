from typing import Literal, Optional
from models.jsonifiable import JSONifiable


PROFESSION_NAMES = Literal[
    "alchemy", "blacksmithing",
    "enchanting", "engineering",
    "herbalism", "inscription",
    "jewelcrafting", "leatherworking",
    "mining", "skinning", "tailoring"
]


class Profession(JSONifiable):
    def __init__(self, name: PROFESSION_NAMES, points: int):
        self.name = name
        self.level = points


class ProfessionPair(JSONifiable):
    def __init__(self,
                 primary: Optional[Profession] = None,
                 secondary: Optional[Profession] = None):

        self.primary = primary
        self.secondary = secondary
