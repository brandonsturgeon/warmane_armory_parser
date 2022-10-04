import time
from typing import Sequence
from models.achievements import AchievementsChunkResponse


dataChunks = [
    {
        "id": "92",
        "category": "General",
    },
    {
        "id": "95",
        "category": "Player vs. Player",
    },
    {
        "id": "165",
        "category": "Player vs. Player",
        "subcategory": "Arena",
    },
]


def get_achievements_content(armoryInterface) -> Sequence[AchievementsChunkResponse]:
    for chunk in dataChunks:
        time.sleep(0.25)
        categoryId = chunk["id"]
        content = armoryInterface.get_post_data("achievements", {"category": categoryId})

        yield AchievementsChunkResponse(
            category=chunk["category"],
            subcategory=chunk.get("subcategory"),
            content=content
        )
