from typing import Dict, Sequence, Union
from parser.armory import ArmoryParser

CLASS_MAP = {
    "death knight": "deathknight"
}

RACE_MAP = {
    "blood elf": "bloodelf",
    "night elf": "nightelf"
}


class CharacterLevelRaceClassParser(ArmoryParser):
    def get_section(self, soup):
        return soup.find(class_="level-race-class")

    def replace_from_map(self,
                         base: str,
                         replacement_map: Dict[str, str]) -> str:

        for k, v in replacement_map.items():
            base = base.replace(k, v)

        return base

    def parse(self) -> Dict[str, Union[str, int]]:
        data: str = self.page.text
        data: str = data.strip()
        data: str = data.lower()
        data: str = self.replace_from_map(data, RACE_MAP)
        data: str = self.replace_from_map(data, CLASS_MAP)
        data: str = data.replace(",", "")

        # ['level', '80', 'tauren', 'warrior', 'icecrown']
        data_spl: Sequence[str] = data.split()

        return {
            "level": int(data_spl[1]),
            "race": data_spl[2],
            "class_name": data_spl[3],
            "realm": data_spl[4]
        }
