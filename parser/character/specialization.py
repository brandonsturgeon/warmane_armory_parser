from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag
from typing import Dict, Literal, Sequence
from models.specialization import Specialization, SpecializationPair
from parser.character.kills import CharacterKillsParser

SPEC_TYPE = Literal["primary", "secondary"]
SPEC_ORDER: Sequence[SPEC_TYPE] = ["primary", "secondary"]


class CharacterSpecializationParser(CharacterKillsParser):

    def get_section(self, soup: BeautifulSoup):
        return soup.find(class_="specialization")

    def parse_stub(self, stub: Tag) -> Specialization:
        name = stub.find(class_="text")
        name = name.find(text=True)
        name = name.strip().lower()

        value = stub.find(class_="value").text

        return Specialization(name=name, points=value)

    def parse(self) -> SpecializationPair:
        spec_data: Dict[SPEC_TYPE, Specialization] = {}
        spec_stubs: ResultSet = self.page.find_all(class_="stub")

        for i in range(len(SPEC_ORDER)):
            which: SPEC_TYPE = SPEC_ORDER[i]
            stub: Tag = spec_stubs[i]

            if not stub:
                continue

            spec_data[which] = self.parse_stub(stub)

        primary = spec_data.get("primary")
        secondary = spec_data.get("secondary")

        return SpecializationPair(
            primary=primary,
            secondary=secondary
        )
