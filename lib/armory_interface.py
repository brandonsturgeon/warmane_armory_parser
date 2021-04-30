from bs4 import BeautifulSoup
import requests


class ArmoryInterface:
    def __init__(self, name, realm):
        self.base_url = f"https://armory.warmane.com/character/{name}/{realm}"

    def get_page(self, page):
        url = f"{self.base_url}/{page}"
        req = requests.get(url)
        content = req.content
        soup = BeautifulSoup(content, "html.parser")

        return soup

    def get_summary_content(self):
        return self.get_page("summary")

    def get_match_history_content(self):
        return self.get_page("match-history")
