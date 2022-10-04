from bs4 import BeautifulSoup
from typing import Sequence
from models.achievements import Achievement, AchievementsGroup, AchievementsChunkResponse


class AchievementsPageParser():
    def __init__(self, chunks: Sequence[AchievementsChunkResponse]):
        self.chunks = chunks

    def parse_achievement(self, achievement: BeautifulSoup) -> Achievement:
        # "ach1235" -> "1235"
        achievementId = achievement.attrs["id"][3:]

        # "\n50\n"
        points = achievement.find("div", "points").text
        # 50
        points = int(points.strip())

        # "http://cdn.warmane.com/wotlk/icons/large/achievement_pvp_h_15.jpg"
        image = achievement.find("img").attrs["src"]
        # "achievement_pvp_h_15.jpg"
        image = image.split("/")[-1]

        name = achievement.find("div", "title").text.strip()
        description = achievement.find("div", "description").text.strip()

        reward = achievement.find("div", "reward")
        if reward is not None:
            reward = reward.text.strip()

        date = achievement.find("div", "date")
        if date is not None:
            # Earned 10/10/2019
            date = date.text.strip()
            # 10/10/2019
            date = date[7:]

        return Achievement(
            id=achievementId,
            name=name,
            description=description,
            date=date,
            points=points,
            image=image,
            reward=reward
        )

    def parse_chunk_content(self, content: BeautifulSoup) -> Sequence[Achievement]:
        achievements = content.find_all("div", "achievement")
        return [self.parse_achievement(achievement) for achievement in achievements]

    def parse_chunk(self, chunk: AchievementsChunkResponse) -> AchievementsGroup:
        return AchievementsGroup(
            category=chunk.category,
            subcategory=chunk.subcategory,
            achievements=self.parse_chunk_content(chunk.content)
        )

    def parse(self) -> Sequence[AchievementsGroup]:
        return [self.parse_chunk(chunk) for chunk in self.chunks]
