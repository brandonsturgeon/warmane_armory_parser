from parser.armory import ArmoryParser
from parser.item.items import ItemsParser
from parser.character.stats import CharacterStatsParser
from parser.character.kills import CharacterKillsParser
from parser.character.professions import CharacterProfessionsParser
from parser.character.specialization import CharacterSpecializationParser
from parser.character.activity import CharacterActivityParser


class CharacterProfileParser(ArmoryParser):
    content_id = "character-profile"

    def get_items(self):
        return ItemsParser(self.page).parse()

    def get_stats(self):
        return CharacterStatsParser(self.page).parse()

    def get_kills(self):
        return CharacterKillsParser(self.page).parse()

    def get_professions(self):
        return CharacterProfessionsParser(self.page).parse()

    def get_specializations(self):
        return CharacterSpecializationParser(self.page).parse()

    def get_activity(self):
        return CharacterActivityParser(self.page).parse()

    def parse(self):
        return {
            "items": self.get_items(),
            "stats": self.get_stats(),
            "kills": self.get_kills(),
            "professions": self.get_professions(),
            "specializations": self.get_specializations(),
            "activity": self.get_activity()
        }
