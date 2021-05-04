from bs4 import BeautifulSoup
from typing import Sequence
from parser.armory import ArmoryParser
from models.activity import Activity


class CharacterActivityParser(ArmoryParser):
    def get_section(self, soup: BeautifulSoup) -> BeautifulSoup:
        return soup.find(class_="recent-activity")

    def extract_id(self, stub: BeautifulSoup) -> str:
        # 'http://wotlk.cavernoftime.com/achievement=2157'
        href: str = stub.a.get("href")

        # ['http://wotlk.cavernoftime.com/achievement', '2157']
        spl: Sequence[str] = href.split("=")

        return spl[-1]

    def extract_name(self, stub: BeautifulSoup) -> str:
        return stub.find(class_="name").text

    def extract_timing(self, stub: BeautifulSoup) -> str:
        return stub.find(class_="time").text

    def parse_stub(self, stub: BeautifulSoup) -> Activity:
        stub_id: str = self.extract_id(stub)
        name: str = self.extract_name(stub)
        timing: str = self.extract_timing(stub)

        return Activity(
            activity_id=stub_id,
            name=name,
            when=timing
        )

    def parse(self) -> Sequence[Activity]:
        stubs = self.page.find_all(class_="stub")
        return [self.parse_stub(stub) for stub in stubs]
