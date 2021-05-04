import json
import random
import re
import time
from typing import Dict
from bs4 import BeautifulSoup
from wotlkdb_interface import WotlkDBInterface
from enchant_ids import EnchantIDs

all_gem_ids = []
with open("lib/data/all_gem_ids.json", "rb") as gem_ids:
    all_gem_ids = json.loads(gem_ids.read())

all_gem_ids_count = len(all_gem_ids)

wotlkdb = WotlkDBInterface()
enchant_ids = EnchantIDs()
gem_data_pattern = re.compile(r'.+\.tooltip_enus = \"(.*)\"')

all_gem_data = {}
ignored_gem_ids = {}


class InvalidGemException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


def parse_colors(colors: str) -> Dict[str, bool]:
    any_color = "any socket" in colors

    red = any_color or "Red" in colors
    blue = any_color or "Blue" in colors
    yellow = any_color or "Yellow" in colors
    meta = any_color or "meta" in colors

    return {
        "red": red,
        "blue": blue,
        "yellow": yellow,
        "meta": meta
    }


def get_name_from_soup(soup: BeautifulSoup) -> str:
    name = soup.find(class_="q4")
    name = name or soup.find(class_="q3")
    name = name or soup.find(class_="q2")

    # Gems unavailable to players
    if not name:
        raise InvalidGemException("No Name found")

    name = name.find(text=True)
    name = name.replace("\\", "")

    return name


def get_colors_from_soup(soup: BeautifulSoup) -> Dict[str, bool]:
    colors = soup.find(class_="q")

    # Raw gem without effect
    if not colors:
        raise InvalidGemException("No Colors found")

    colors = colors.find(text=True)
    colors = parse_colors(colors)

    return colors


def get_enchant_id_from_soup(soup: BeautifulSoup) -> str:
    link = soup.find("a")
    if not link:
        raise InvalidGemException("No enchant link found")

    enchant_link = link.get("href")
    if not enchant_link:
        raise InvalidGemException("No enchant link found")

    enchant_id = enchant_link.split("=")[-1]

    return enchant_id


def get_effect_for_enchant_id(enchant_id: str) -> str:
    return enchant_ids.get(enchant_id)


def get_data_for_item(gem_id: str):
    page_data: bytes = wotlkdb.get_item(gem_id, xml=True)
    soup: BeautifulSoup = BeautifulSoup(page_data, "lxml")
    soup = soup.find("htmltooltip")

    name: str = get_name_from_soup(soup)
    colors: Dict[str, bool] = get_colors_from_soup(soup)
    enchant_id: str = get_enchant_id_from_soup(soup)
    effect: str = get_effect_for_enchant_id(enchant_id)

    return {
        "name": name,
        "colors": colors,
        "effect": effect,
        "enchant_id": enchant_id
    }


def estimated_time_remaining(i: int) -> int:
    return (all_gem_ids_count - i) * 2


def sleep():
    sleep_time = random.uniform(1.0, 3.0)
    print(f"Sleeping for {round(sleep_time, 2)} seconds")
    time.sleep(sleep_time)


if __name__ == "__main__":
    for i, gem_id in enumerate(all_gem_ids):
        print()
        print()

        adjusted_index = i + 1
        remaining = estimated_time_remaining(i)
        progress = f"{adjusted_index} / {all_gem_ids_count}"
        timing_info = f"{progress} | ~{remaining} seconds remaining"
        print(f"Getting data for {gem_id} ({timing_info})")

        data = None
        try:
            data = get_data_for_item(gem_id)
        except InvalidGemException as e:
            message = e.message

            print(f"Gem was invalid, ignoring.. ({message})")
            ignored_gem_ids[gem_id] = message

            sleep()
            continue

        print(data)
        all_gem_data[gem_id] = data

        sleep()

    ignored_count = len(ignored_gem_ids)
    print(f"Ignored {ignored_count} invalid gems")
    print(ignored_gem_ids)

    successful_count = len(all_gem_data)
    print(f"Scraped {successful_count} valid gems, attempting to save to file")

    dumped = json.dumps(all_gem_data)
    print(dumped)
    print()
    print()
    print()

    with open("gem_data.json", "w") as gem_data_file:
        gem_data_file.write(dumped)

    print("Successfully wrote gem data to file!")
