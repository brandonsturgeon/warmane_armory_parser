from typing import Literal, Optional, Sequence
from models.jsonifiable import JSONifiable
from models.glyph import Glyph

TALENT_TREE_NAMES = Literal[
    "blood", "frost", "unholy",                   # Death Knight
    "balance", "feral", "restoration",            # Druid
    "beast mastery", "marksmanship", "survival",  # Hunter
    "arcane", "fire", "frost",                    # Mage
    "holy", "protection", "retribution",          # Paladin
    "discipline", "holy", "shadow",               # Priest
    "assassination", "combat", "subtlety",        # Rogue
    "elemental", "enhancement", "restoration",    # Shaman
    "affliction", "demonology", "destruction",    # Warlock
    "arms", "fury", "protection"                  # Warrior
]


class Talent(JSONifiable):
    """
        Represents a single talent node
    """
    def __init__(self,
                 talent_id: str,
                 current_points: int,
                 max_points: int):

        self.id = talent_id
        self.current = current_points
        self.max = max_points


class TalentTree(JSONifiable):
    """
        Represents a single tree, comprised of many rows
    """
    def __init__(self,
                 name: TALENT_TREE_NAMES,
                 rows: Sequence[Sequence[Talent]]):

        self.name = name
        self.rows = rows


class TalentSpec(JSONifiable):
    """
        Represents the three trees and
        six glyphs that comprise a single spec
    """
    def __init__(self,
                 tree1: TalentTree,
                 tree2: TalentTree,
                 tree3: TalentTree,
                 major_glyphs: Sequence[Glyph],
                 minor_glyphs: Sequence[Glyph]):

        self.tree1 = tree1
        self.tree2 = tree2
        self.tree3 = tree3
        self.major_glyphs = major_glyphs
        self.minor_glyphs = minor_glyphs


class PlayerSpec(JSONifiable):
    """
        Represents two specs, three trees each
    """
    def __init__(self,
                 spec1: Optional[TalentSpec],
                 spec2: Optional[TalentSpec]):

        self.spec1 = spec1
        self.spec2 = spec2
