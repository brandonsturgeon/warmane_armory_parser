import time
from typing import Sequence
from models.statistics import StatisticsChunkResponse


dataChunks = [
    {
        "id": "136",
        "category": "Kills",
        "subcategory": "Honorable Kills"
    },

    {
        "id": "137",
        "category": "Kills",
        "subcategory": "Killing Blows"
    },

    {
        "id": "15062",
        "category": "Dungeons & Raids",
        "subcategory": "Fall of the Lich King"
    },

    {
        "id": "134",
        "category": "Travel"
    },

    {
        "id": "21",
        "category": "Player vs. Player",
    },

    {
        "id": "152",
        "category": "Player vs. Player",
        "subcategory": "Rated Arenas"
    },

    {
        "id": "153",
        "category": "Player vs. Player",
        "subcategory": "Battlegrounds"
    },

    {
        "id": "154",
        "category": "Player vs. Player",
        "subcategory": "World"
    },
]


def get_statistics_content(armoryInterface) -> Sequence[StatisticsChunkResponse]:
    for chunk in dataChunks:
        time.sleep(0.25)
        categoryId = chunk["id"]
        content = armoryInterface.get_post_data("statistics", {"category": categoryId})

        yield StatisticsChunkResponse(
            category=chunk["category"],
            subcategory=chunk.get("subcategory"),
            content=content
        )
