from parser.armory import ArmoryParser
from parser.character.level_race_class import CharacterLevelRaceClassParser
from parser.character.profile import CharacterProfileParser


class SummaryPageParser(ArmoryParser):
    content_id = "character-sheet"

    def get_name(self):
        name = self.page.find(class_="name").find(text=True).strip()
        return {"name": name}

    def get_guild_name(self):
        guild_name = self.page.find(class_="guild-name")
        guild_name = guild_name.find(text=True).strip()

        return {"guild-name": guild_name}

    def get_level_race_class(self):
        return CharacterLevelRaceClassParser(self.page).parse()

    def get_achievement_points(self):
        points = self.page.find(class_="achievement-points").text
        points = points.strip()

        return {"achievement-points": int(points)}

    def get_character_profile(self):
        return CharacterProfileParser(self.page).parse()

    def parse(self):
        summary = {}

        summary.update(self.get_name())
        summary.update(self.get_guild_name())
        summary.update(self.get_level_race_class())
        summary.update(self.get_achievement_points())
        summary.update(self.get_character_profile())

        return summary
