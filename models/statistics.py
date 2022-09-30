from bs4 import BeautifulSoup
from typing import Literal, Optional, Sequence
from models.jsonifiable import JSONifiable

Category = Literal[
    "Summary", "Character", "Combat",
    "Kills", "Deaths", "Quests",
    "Dungeons & Raids", "Skills", "Travel",
    "Social", "Player vs. Player"
]

Subcategory = Literal[
    # Character
    "Wealth", "Consumables", "Reputation", "Gear",

    # Kills
    "Creatures", "Honorable Kills", "Killing Blows",

    # Deaths
    "Arenas", "Battlegrounds", "Dungeon", "World", "Resurrection",

    # Dungeons & Raids
    "Classic", "The Burning Crusade", "Wrath of the Lich King",
    "Secrets of Ulduar", "Call of the Crusade", "Fall of the Lich King",

    # Skills
    "Secondary Skills", "Professions",

    # Player vs. Player
    "Rated Arenas", "Battlegrounds", "World"
]


class Statistic(JSONifiable):
    def __init__(self, name: str, value: str = "- -"):
        self.name = name
        self.value = value


class StatisticsGroup(JSONifiable):
    def __init__(
            self,
            category: Category,
            subcategory: Optional[Subcategory],
            statistics: Sequence[Statistic]):
        self.category = category
        self.subcategory = subcategory
        self.statistics = statistics


class StatisticsChunkResponse:
    """
    DTO for the response of the statistics chunk
    """
    def __init__(
            self,
            category: Category,
            subcategory: Optional[Subcategory],
            content: BeautifulSoup):
        self.content = content
        self.category: Category = category
        self.subcategory: Optional[Subcategory] = subcategory
