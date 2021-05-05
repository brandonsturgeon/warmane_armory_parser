from parser.armory import ArmoryParser
from models.talent import PlayerSpec
from parser.talents.player_spec import PlayerSpecParser


class TalentPageParser(ArmoryParser):
    content_id = "character-sheet"

    def parse(self) -> PlayerSpec:
        return PlayerSpecParser(self.page).parse()
