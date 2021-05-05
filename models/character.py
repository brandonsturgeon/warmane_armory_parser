from typing import Optional, Sequence
from models.jsonifiable import JSONifiable
from models.equipped_items import EquippedItems
from models.activity import Activity
from models.profession import ProfessionPair
from models.specialization import SpecializationPair
from models.talent import PlayerSpec
from models.stats_group import StatsGroup
from models.skills import SkillSet
from models.kills import KillsInfo
from models.meta_stats import RACE_TYPES, CLASS_TYPES


class Character(JSONifiable):
    def __init__(self,
                 name: str,
                 guild_name: str,
                 achievement_points: int,
                 level: int,
                 race: RACE_TYPES,
                 class_name: CLASS_TYPES,
                 realm: str,
                 items: EquippedItems,
                 stats: StatsGroup,
                 kills: KillsInfo,
                 professions: ProfessionPair,
                 skills: SkillSet,
                 specializations: SpecializationPair,
                 talents: Optional[PlayerSpec],
                 activity: Sequence[Activity]):

        self.name = name
        self.guild_name = guild_name
        self.achievement_points = achievement_points
        self.level = level
        self.race = race
        self.class_name = class_name
        self.realm = realm
        self.items = items
        self.stats = stats
        self.kills = kills
        self.profesions = professions
        self.skills = skills
        self.specializations = specializations
        self.talents = talents
        self.activity = activity
