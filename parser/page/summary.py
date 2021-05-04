from bs4 import BeautifulSoup
from typing import Dict, Union
from models.meta_stats import MetaStats
from parser.armory import ArmoryParser
from parser.character.level_race_class import CharacterLevelRaceClassParser
from parser.character.profile import CharacterProfileParser


class SummaryPageParser(ArmoryParser):
    content_id = "character-sheet"

    def get_name(self) -> str:
        name: str = self.page.find(class_="name").find(text=True).strip()
        return name

    def get_guild_name(self) -> str:
        guild_name: BeautifulSoup = self.page.find(class_="guild-name")
        formatted_guild_name: str = guild_name.find(text=True).strip()

        return formatted_guild_name

    def get_level_race_class(self) -> Dict[str, Union[str, int]]:
        return CharacterLevelRaceClassParser(self.page).parse()

    def get_achievement_points(self) -> int:
        points: str = self.page.find(class_="achievement-points").text
        points: str = points.strip()

        return int(points)

    def get_character_profile(self):
        return CharacterProfileParser(self.page).parse()

    def parse(self):
        summary = {}

        summary["name"] = self.get_name()
        summary["guild_name"] = self.get_guild_name()
        summary["achievement_points"] = self.get_achievement_points()

        summary.update(self.get_level_race_class())
        summary.update(self.get_character_profile())

        return summary
