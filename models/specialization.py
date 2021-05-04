from typing import Literal, Optional
from models.jsonifiable import JSONifiable


SPEC_NAMES = Literal[
    "blood", "frost", "unholy",  # Death Knight
    "balance", "feral", "restoration",  # Druid
    "beast mastery", "marksmanship", "survival",  # Hunter
    "arcane", "fire", "frost",  # Mage
    "holy", "protection", "retribution",  # Paladin
    "discipline", "holy", "shadow",  # Priest
    "assassination", "combat", "subtlety",  # Rogue
    "elemental", "enhancement", "restoration",  # Shaman
    "affliction", "demonology", "destruction",  # Warlock
    "arms", "fury", "protection"  # Warrior
]


class Specialization(JSONifiable):
    def __init__(self, name: SPEC_NAMES, points: str):
        self.name = name
        self.points = points


class SpecializationPair(JSONifiable):
    def __init__(self,
                 primary: Optional[Specialization],
                 secondary: Optional[Specialization]):

        self.primary = primary
        self.secondary = secondary
