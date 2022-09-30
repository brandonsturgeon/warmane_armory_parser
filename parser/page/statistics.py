from bs4 import BeautifulSoup
from typing import Sequence
from models.statistics import Statistic, StatisticsGroup, StatisticsChunkResponse


class StatisticsPageParser():
    def __init__(self, chunks: Sequence[StatisticsChunkResponse]):
        self.chunks = chunks

    def parse_chunk_content(self, content: BeautifulSoup) -> Sequence[Statistic]:
        # [<td>Name</td>, <td>Value</td>, <td>Name</td>, <td>Value</td>, ...]
        tds = content.find_all("td")

        # [Name, Value, Name, Value, ...]
        tds = [td.text for td in tds]

        # {Name: Value, Name: Value, ...}
        pairs = dict(zip(tds[::2], tds[1::2]))

        return [Statistic(name, value) for name, value in pairs.items()]

    def parse_chunk(self, chunk: StatisticsChunkResponse) -> StatisticsGroup:
        return StatisticsGroup(
            category=chunk.category,
            subcategory=chunk.subcategory,
            statistics=self.parse_chunk_content(chunk.content)
        )

    def parse(self) -> Sequence[StatisticsGroup]:
        return [self.parse_chunk(chunk) for chunk in self.chunks]
