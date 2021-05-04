from typing import Dict, Literal, Union
from parser.armory import ArmoryParser
from models.kills import KillsInfo

KILL_TYPES = Literal["total-kills", "today"]


class CharacterKillsParser(ArmoryParser):
    def get_section(self, soup):
        return soup.find(class_="pvpbasic")

    def parse_stub(self, stub) -> Dict[KILL_TYPES, Union[int, str]]:
        # 'total kills\n                    1387'
        stub_text = stub.text.strip().lower()

        # ['total kills', '                    1387']
        name, value = stub_text.split("\n")

        # 'total-kills'
        name = name.replace(" ", "-")

        # '1387'
        value = value.strip()

        # 1387
        value = self.try_int(value)

        return {name: value}

    def parse(self) -> KillsInfo:
        kill_data = {}
        pvp_stubs = self.page.find_all(class_="stub")

        for stub in pvp_stubs:
            stub_data = self.parse_stub(stub)
            kill_data.update(stub_data)

        return KillsInfo(
            all_time=kill_data["total-kills"],
            today=kill_data["kills-today"]
        )
