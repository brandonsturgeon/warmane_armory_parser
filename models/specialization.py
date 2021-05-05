"""
Used for the quick-access talent info on the Summary page
"""

from typing import Optional
from models.jsonifiable import JSONifiable
from models.talent import TALENT_TREE_NAMES


class Specialization(JSONifiable):
    def __init__(self, name: TALENT_TREE_NAMES, points: str):
        self.name = name
        self.points = points


class SpecializationPair(JSONifiable):
    def __init__(self,
                 primary: Optional[Specialization],
                 secondary: Optional[Specialization]):

        self.primary = primary
        self.secondary = secondary
