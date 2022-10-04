import requests
from typing import Dict, Sequence
from bs4 import BeautifulSoup
from models.statistics import StatisticsChunkResponse
from models.achievements import AchievementsChunkResponse
from lib.statistics_generator import get_statistics_content
from lib.achievements_generator import get_achievements_content


class ArmoryInterface:
    def __init__(self, name: str, realm: str):
        self.base_url = f"https://armory.warmane.com/character/{name}/{realm}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
        }

    def get_page(self, page: str) -> BeautifulSoup:
        url = f"{self.base_url}/{page}"
        req: requests.models.Response = requests.get(url, headers=self.headers)
        content: bytes = req.content
        soup = BeautifulSoup(content, "html.parser")

        return soup

    def get_post_data(self, page: str, data: Dict[str, str]) -> BeautifulSoup:
        url = f"{self.base_url}/{page}"
        req: requests.models.Response = requests.post(url, data=data, headers=self.headers)
        content: str = req.json()["content"]
        soup = BeautifulSoup(content, "html.parser")

        return soup

    def get_summary_content(self) -> BeautifulSoup:
        return self.get_page("summary")

    def get_match_history_content(self) -> BeautifulSoup:
        return self.get_page("match-history")

    def get_talent_content(self) -> BeautifulSoup:
        return self.get_page("talents")

    def get_statistics_content(self) -> Sequence[StatisticsChunkResponse]:
        return get_statistics_content(self)

    def get_achievements_content(self) -> Sequence[AchievementsChunkResponse]:
        return get_achievements_content(self)

    def get_mount_and_companion_content(self) -> BeautifulSoup:
        return self.get_page("mounts-and-companions")
