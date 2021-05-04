import requests
from time import time


class RateLimitedException(Exception):
    def __init__(self):
        self.message = "Can't scrape yet"


class WotlkDBInterface:
    def __init__(self):
        self.base_url = "https://wotlkdb.com"
        self.scrape_delay = 1
        self.last_scrape = 0

    def can_scrape(self) -> bool:
        return time() >= (self.last_scrape + self.scrape_delay)

    def get_item(self, item_id: str, xml: bool = False) -> bytes:
        if not self.can_scrape():
            raise RateLimitedException

        xml_param = "&xml" if xml else ""
        url = f"{self.base_url}/?item={item_id}{xml_param}"
        req = requests.get(url)
        self.last_scrape = time()

        return req.content
