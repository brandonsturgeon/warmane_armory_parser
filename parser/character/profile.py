from typing import Dict, Union

from models.profession import ProfessionPair
from models.skills import SkillSet
from models.stats_group import StatsGroup
from models.specialization import SpecializationPair
from models.kills import KillsInfo

from models.equipped_items import EquippedItems
from parser.armory import ArmoryParser
from parser.item.items import ItemsParser
from parser.character.stats import CharacterStatsParser
from parser.character.kills import CharacterKillsParser
from parser.character.professions import CharacterProfessionsParser
from parser.character.skills import CharacterSkillParser
from parser.character.specialization import CharacterSpecializationParser
from parser.character.activity import CharacterActivityParser


class CharacterProfileParser(ArmoryParser):
    content_id = "character-profile"

    def get_items(self) -> EquippedItems:
        return ItemsParser(self.page).parse()

    def get_stats(self) -> StatsGroup:
        return CharacterStatsParser(self.page).parse()

    def get_kills(self) -> KillsInfo:
        return CharacterKillsParser(self.page).parse()

    def get_professions(self) -> ProfessionPair:
        return CharacterProfessionsParser(self.page).parse()

    def get_skills(self) -> SkillSet:
        return CharacterSkillParser(self.page).parse()

    def get_specializations(self) -> SpecializationPair:
        return CharacterSpecializationParser(self.page).parse()

    def get_activity(self):
        return CharacterActivityParser(self.page).parse()

    def parse(self):
        return {
            "items": self.get_items(),
            "stats": self.get_stats(),
            "kills": self.get_kills(),
            "professions": self.get_professions(),
            "skills": self.get_skills(),
            "specializations": self.get_specializations(),
            "activity": self.get_activity()
        }
