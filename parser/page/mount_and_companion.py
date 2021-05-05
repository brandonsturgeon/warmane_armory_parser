from bs4.element import ResultSet, Tag
from typing import Sequence
from parser.armory import ArmoryParser
from models.mount import Mount


class MountAndCompanionPageParser(ArmoryParser):
    content_id = "mount-tab"

    def parse_mount(self, mount: Tag) -> Mount:
        link_tag: Tag = mount.find("a")
        mount_id: str = link_tag.get("href").split("=")[-1]
        name: str = link_tag.find(text=True)

        return Mount(
            mount_id=mount_id,
            name=name
        )

    def parse(self) -> Sequence[Mount]:
        all_mounts: ResultSet = self.page.find_all(class_="basic")
        return [self.parse_mount(mount) for mount in all_mounts]
