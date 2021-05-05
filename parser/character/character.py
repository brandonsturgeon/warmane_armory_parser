from models.character import Character
from lib.armory_interface import ArmoryInterface
from parser.page.summary import SummaryPageParser
from parser.page.talents import PlayerSpecParser
from parser.page.mount_and_companion import MountAndCompanionPageParser


class CharacterParser:
    def __init__(self, name: str, realm: str = "Icecrown"):
        self.character_name: str = name
        self.realm: str = realm

    def build_character(self):
        character_armory = ArmoryInterface(self.character_name, self.realm)

        summary_content = character_armory.get_summary_content()
        summary_data = SummaryPageParser(summary_content).parse()

        talent_content = character_armory.get_talent_content()
        talent_data = PlayerSpecParser(talent_content).parse()

        mount_content = character_armory.get_mount_and_companion_content()
        mount_data = MountAndCompanionPageParser(mount_content).parse()

        return Character(
            **summary_data,
            talents=talent_data,
            mounts=mount_data
        )
