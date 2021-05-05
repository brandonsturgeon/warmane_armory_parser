from typing import Literal
from models.jsonifiable import JSONifiable
GLYPH_NAMES = Literal["major", "minor"]


class Glyph(JSONifiable):
    def __init__(self,
                 glyph_id: str,
                 name: str):

        self.id = glyph_id
        self.name = name
