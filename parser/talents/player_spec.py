from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag
from typing import Dict, Sequence
from parser.armory import ArmoryParser
from parser.talents.glyphs import GlyphParser
from models.glyph import Glyph
from models.talent import (
    Talent,
    TalentRow,
    TalentTree,
    TalentSpec,
    PlayerSpec,
    TALENT_TREE_NAMES
)


class PlayerSpecParser(ArmoryParser):
    def get_section(self, soup: BeautifulSoup) -> Tag:
        return soup

    def parse_talent_id(self, talent_link: str) -> str:
        return talent_link.split("=")[1]

    def parse_node(self, node: Tag) -> Talent:
        talent_link: str = node.get("href")
        talent_id: str = self.parse_talent_id(talent_link)

        points_tag: Tag = node.find(class_="talent-points")
        points: str = points_tag.find(text=True).strip()

        points_spl: Sequence[str] = points.split("/")
        current_points: int = int(points_spl[0])
        max_points: int = int(points_spl[1])

        return Talent(
            talent_id=talent_id,
            current_points=current_points,
            max_points=max_points
        )

    def parse_row(self, tier: Tag) -> TalentRow:
        nodes: ResultSet = tier.find_all(class_="talent")
        row: Sequence[Talent] = [self.parse_node(node) for node in nodes]

        return TalentRow(talents=row)

    def get_name_from_tree(self, tree: Tag) -> TALENT_TREE_NAMES:
        info: Tag = tree.find(class_="talent-tree-info")
        info_span: Tag = info.find("span")
        tree_name = info_span.text
        formatted_tree_name: TALENT_TREE_NAMES = tree_name.lower()

        return formatted_tree_name

    def parse_tree(self, tree: Tag) -> TalentTree:
        tiers: ResultSet = tree.find_all(class_="tier")
        rows: Sequence[TalentRow] = [self.parse_row(tier) for tier in tiers]
        name = self.get_name_from_tree(tree)

        return TalentTree(name=name, rows=rows)

    def parse_spec(self, spec: Tag, spec_id: int) -> TalentSpec:
        nodes: ResultSet = spec.find_all(class_="talent-tree")
        trees: Sequence[TalentTree] = [self.parse_tree(tree) for tree in nodes]
        glyphs = GlyphParser(self.page).parse(spec_id)

        return TalentSpec(
            tree1=trees[0],
            tree2=trees[1],
            tree3=trees[2],
            major_glyphs=glyphs["major"],
            minor_glyphs=glyphs["minor"]
        )

    def parse(self) -> PlayerSpec:
        spec1_node: Tag = self.page.find(id="spec-0")
        spec2_node: Tag = self.page.find(id="spec-1")

        spec1 = None
        spec2 = None

        if spec1_node:
            spec1 = self.parse_spec(spec1_node, 0)

        if spec2_node:
            spec2 = self.parse_spec(spec2_node, 1)

        return PlayerSpec(
            spec1=spec1,
            spec2=spec2
        )
