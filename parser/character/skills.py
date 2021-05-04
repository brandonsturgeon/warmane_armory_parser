from typing import Dict, Union
from bs4 import BeautifulSoup
from bs4.element import ResultSet
from parser.character.kills import CharacterKillsParser
from models.skills import SkillSet, SKILLS_TYPE


class CharacterSkillParser(CharacterKillsParser):
    def get_section(self, soup: BeautifulSoup) -> Union[ResultSet, None]:
        section = soup.find_all(class_="profskills")

        # The first "profskills" is their primary professions
        if len(section) == 1:
            return

        return section[1]

    def format_skill(self, value: str) -> int:
        skill_value: str = value.split(" / ")[0]
        skill_number: Union[str, int] = int(skill_value)

        return skill_number

    def parse_stub(self, stub) -> Dict[SKILLS_TYPE, int]:
        # 'total kills\n                    1387'
        stub_text = stub.text.strip().lower()

        # ['total kills', '                    1387']
        name, value = stub_text.split("\n")

        # 'total-kills'
        name = name.replace(" ", "_")
        name = name.lower()

        # '1387'
        value: str = value.strip()
        formatted_value: int = self.format_skill(value)

        return {name: formatted_value}

    def parse(self) -> SkillSet:
        if not self.page:
            return SkillSet()

        skills: Dict[str, int] = {}
        pvp_stubs = self.page.find_all(class_="stub")

        for stub in pvp_stubs:
            stub_data = self.parse_stub(stub)
            skills.update(stub_data)

        return SkillSet(**skills)
