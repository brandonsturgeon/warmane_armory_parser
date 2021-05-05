from typing import Literal, Optional, Union
from models.jsonifiable import JSONifiable

STATS_CATEGORIES = Literal[
    "melee",
    "ranged",
    "spell",
    "attributes",
    "defense",
    "resistances"
]


class AttackStats(JSONifiable):
    def __init__(self,
                 damage: Optional[str] = None,
                 power: Optional[int] = None,
                 speed: Optional[int] = None,
                 hit: Optional[str] = None,
                 critical: Optional[str] = None):

        self.damage = damage
        self.power = power
        self.speed = speed
        self.hit_rating = hit
        self.critical = critical


class MeleeStats(AttackStats):
    pass


class RangedStats(AttackStats):
    pass


class SpellStats(JSONifiable):
    def __init__(self,
                 power: Optional[int] = None,
                 healing: Optional[int] = None,
                 haste: Optional[str] = None,
                 hit: Optional[str] = None,
                 critical: Optional[str] = None):

        self.power = power
        self.healing = healing
        self.haste = haste
        self.hit_rating = hit
        self.critical = critical


class AttributesStats(JSONifiable):
    def __init__(self,
                 strength: Optional[int] = None,
                 agility: Optional[int] = None,
                 intellect: Optional[int] = None,
                 stamina: Optional[int] = None,
                 spirit: Optional[int] = None,
                 expertise: Optional[int] = None):

        self.strength = strength
        self.agility = agility
        self.intellect = intellect
        self.stamina = stamina
        self.spirit = spirit
        self.expertise = expertise


class DefenseStats(JSONifiable):
    def __init__(self,
                 armor: Optional[int] = None,
                 dodge: Optional[str] = None,
                 parry: Optional[str] = None,
                 block: Optional[str] = None,
                 resilience: Optional[int] = None):

        self.armor = armor
        self.dodge = dodge
        self.parry = parry
        self.block = block
        self.resilience = resilience


class ResistanceStats(JSONifiable):
    def __init__(self,
                 arcane: Optional[int] = None,
                 fire: Optional[int] = None,
                 nature: Optional[int] = None,
                 frost: Optional[int] = None,
                 shadow: Optional[int] = None):

        self.arcane = arcane
        self.fire = fire
        self.nature = nature
        self.frost = frost
        self.shadow = shadow


STATS_MAP = {
    "melee": MeleeStats,
    "ranged": RangedStats,
    "spell": SpellStats,
    "attributes": AttributesStats,
    "defense": DefenseStats,
    "resistances": ResistanceStats
}

STATS_GROUPS = Union[
    MeleeStats,
    RangedStats,
    SpellStats,
    AttributesStats,
    DefenseStats,
    ResistanceStats
]


class StatsGroup(JSONifiable):
    def __init__(self,
                 melee: Optional[MeleeStats] = None,
                 ranged: Optional[RangedStats] = None,
                 spell: Optional[SpellStats] = None,
                 attributes: Optional[AttributesStats] = None,
                 defense: Optional[DefenseStats] = None,
                 resistances: Optional[ResistanceStats] = None):

        self.melee = melee
        self.ranged = ranged
        self.spell = spell
        self.attributes = attributes
        self.defense = defense
        self.resistances = resistances

    def set_category(self, category: STATS_CATEGORIES, data: STATS_GROUPS):
        setattr(self, category, data)
