from typing import Dict, Sequence
from bs4.element import ResultSet, Tag
from parser.armory import ArmoryParser
from models.glyph import Glyph, GLYPH_NAMES
glyphs_type = Sequence[Glyph]


class GlyphParser(ArmoryParser):
    def get_section(self, soup: Tag):
        return soup.find(class_="character-glyphs")

    def parse_glyph(self, glyph_wrapper: Tag) -> Glyph:
        glyph: Tag = glyph_wrapper.find("a")

        url = glyph.get("href")
        glyph_id = url.split("=")[-1]
        glyph_name = glyph.find(text=True)

        return Glyph(
            glyph_id=glyph_id,
            name=glyph_name
        )

    def parse(self, spec_id: int) -> Dict[GLYPH_NAMES, glyphs_type]:
        spec_glyphs: ResultSet = self.page.find_all("div")[spec_id]

        major_nodes: ResultSet = spec_glyphs.find_all(class_="glyph major")
        major_glyphs: glyphs_type = [
            self.parse_glyph(glyph) for glyph in major_nodes
        ]

        minor_nodes: ResultSet = spec_glyphs.find_all(class_="glyph minor")
        minor_glyphs: glyphs_type = [
            self.parse_glyph(glyph) for glyph in minor_nodes
        ]

        return {
            "major": major_glyphs,
            "minor": minor_glyphs
        }
