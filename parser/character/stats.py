import bs4
from bs4 import BeautifulSoup
from typing import Dict, Union
from parser.armory import ArmoryParser
from models.stats_group import (
    StatsGroup,
    STATS_CATEGORIES,
    STATS_GROUPS,
    STATS_MAP
)

PARSED_STATS_TYPE = Dict[STATS_CATEGORIES, STATS_GROUPS]


class CharacterStatsParser(ArmoryParser):
    def get_section(self, soup: BeautifulSoup):
        return soup.find(class_="character-stats")

    def parse_stub(self, stub: bs4.element.Tag) -> PARSED_STATS_TYPE:
        stats: PARSED_STATS_TYPE = {}

        category: str = ""
        stub_text_lines: list[str] = stub.text.split("\n")

        for line in stub_text_lines:
            stripped: str = line.strip().lower()

            if len(stripped) == 0:
                continue

            # New Category (each stat has a : in the line)
            if ":" not in stripped:
                category: str = stripped
                stats[category]: STATS_GROUPS = STATS_MAP[category]()
                continue

            spl: list[str] = stripped.split(": ")

            name: str = spl[0]
            name: str = name.replace(" ", "_")

            value: str = spl[1]
            value: Union[str, int] = self.try_int(value)
            setattr(stats[category], name, value)

        return stats

    def parse(self) -> StatsGroup:
        stats = StatsGroup()
        stubs: bs4.element.ResultSet = self.page.find_all(class_="stub")

        for stub in stubs:
            stub_stats: PARSED_STATS_TYPE = self.parse_stub(stub)

            for category, stats_group in stub_stats.items():
                stats.set_category(category, stats_group)

        return stats
