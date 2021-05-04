from typing import Literal
from models.jsonifiable import JSONifiable

RACE_TYPES = Literal[
    "draenei", "dwarf", "gnome", "human", "nightelf",
    "bloodelf", "orc", "tauren", "troll", "undead"
]

CLASS_TYPES = Literal[
    "deathknight", "druid", "hunter", "mage", "paladin",
    "priest", "rogue", "shaman", "warlock", "warrior"
]


class MetaStats(JSONifiable):
    def __init__(self,
                 level: int,
                 race: RACE_TYPES,
                 class_name: CLASS_TYPES,
                 realm: str):

        self.level = level
        self.race = race
        self.class_name = class_name
        self.realm = realm
