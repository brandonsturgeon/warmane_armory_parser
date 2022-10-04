from bs4 import BeautifulSoup
from typing import Literal, Optional, Sequence
from models.jsonifiable import JSONifiable

Category = Literal[
    "Summary", "General", "Quests",
    "Exploration", "Player vs. Player", "Dungeons & Raids",
    "Professions", "Reputation", "World Events", "Feats of Strength"
]

Subcategory = Literal[
    # Quests
    "Classic", "Burning Crusade", "Wrath of the Lich King",

    # Exploration
    "Eastern Kingdoms", "Kalimdor", "Outland", "Northrend",

    # Player vs. Player
    "Arena", "Alterac Valley", "Arathi Basin", "Eye of the Storm",
    "Warsong Gulch", "Strand of the Ancients", "Wintergrasp", "Isle of Conquest",

    # Dungeons & Raids
    "Classic", "The Burning Crusade", "Lich King Dungeon",
    "Lich King Heroic", "Lich King 10-Player Raid", "Lich King 25-Player Raid",
    "Secrets of Ulduar 10", "Secrets of Ulduar 25", "Call of the Crusade 10",
    "Call of the Crusade 25", "Fall of the Lich King 10", "Fall of the Lich King 25",

    # Professions
    "Cooking", "Fishing", "First Aid",

    # Reputation
    "Classic", "Burning Crusade", "Wrath of the Lich King",

    # World Events
    "Lunar Festial", "Love is in the Air", "Noblegarden",
    "Children's Week", "Midsummer", "Brewfest", "Hallow's End",
    "Pilgrim's Bounty", "Winter Veil", "Argent Tournament",
]


class Achievement(JSONifiable):
    def __init__(
            self,
            id: str,
            name: str,
            description: str,
            points: int,
            image: str,
            date: Optional[str],
            reward: Optional[str]):
        self.id = id
        self.name = name
        self.description = description
        self.points = points
        self.image = image
        self.date = date
        self.reward = reward


class AchievementsGroup(JSONifiable):
    def __init__(
            self,
            category: Category,
            subcategory: Optional[Subcategory],
            achievements: Sequence[Achievement]):
        self.category = category
        self.subcategory = subcategory
        self.achievements = achievements


class AchievementsChunkResponse(JSONifiable):
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
