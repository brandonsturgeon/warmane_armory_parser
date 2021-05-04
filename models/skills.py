from typing import Literal, Optional
from models.jsonifiable import JSONifiable

SKILLS_TYPE = Literal["cooking", "fishing", "first_aid"]


class SkillSet(JSONifiable):
    def __init__(self,
                 cooking: Optional[int] = None,
                 fishing: Optional[int] = None,
                 first_aid: Optional[int] = None):

        self.cooking = cooking
        self.fishing = fishing
        self.first_aid = first_aid
