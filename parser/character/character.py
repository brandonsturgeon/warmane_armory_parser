from lib.armory_interface import ArmoryInterface
from parser.page.summary import SummaryPageParser


class CharacterParser:
    def __init__(self, name, realm="Icecrown"):
        self.character_name = name
        self.realm = realm

    def get_info(self):
        character_data = {}
        character_armory = ArmoryInterface(self.character_name, self.realm)

        summary_content = character_armory.get_summary_content()
        character_data["summary"] = SummaryPageParser(summary_content).parse()

        return character_data
