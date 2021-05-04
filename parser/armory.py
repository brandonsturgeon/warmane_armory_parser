from bs4 import BeautifulSoup
from typing import Union


class ArmoryParser:
    def __init__(self, soup: BeautifulSoup):
        self.soup: BeautifulSoup = soup
        self.page: BeautifulSoup = self.get_section(soup)

    def try_int(self, value: str) -> Union[str, int]:
        try:
            return int(value)
        except ValueError:
            return value

    def get_section(self, soup: BeautifulSoup) -> BeautifulSoup:
        return soup.find(id=self.content_id)

    def parse(self):
        raise NotImplementedError
