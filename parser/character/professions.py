from typing import Union
from bs4 import BeautifulSoup
from bs4.element import ResultSet
from parser.character.kills import CharacterKillsParser
from models.profession import Profession, ProfessionPair, PROFESSION_NAMES


class CharacterProfessionsParser(CharacterKillsParser):
    def get_section(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find(class_="profskills")

    def format_prof(self, value: str) -> int:
        skill_value: str = value.split(" / ")[0]
        formatted_value: int = int(skill_value)

        return formatted_value

    def parse(self) -> ProfessionPair:
        professions = []
        pvp_stubs = self.page.find_all(class_="stub")

        for stub in pvp_stubs:
            stub_data: ResultSet = self.parse_stub(stub)
            name: PROFESSION_NAMES = list(stub_data)[0]
            points = self.format_prof(stub_data[name])

            profession = Profession(
                name=name,
                points=points
            )

            professions.append(profession)

        return ProfessionPair(
            primary=professions[0],
            secondary=professions[1] if len(professions) > 1 else None
        )
