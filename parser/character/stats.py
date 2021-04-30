from parser.armory import ArmoryParser


class CharacterStatsParser(ArmoryParser):
    def get_section(self, soup):
        return soup.find(class_="character-stats")

    def parse_stub(self, stub):
        stats = {}

        category = None
        stub_text_lines = stub.text.split("\n")
        for line in stub_text_lines:
            stripped = line.strip().lower()

            if len(stripped) == 0:
                continue

            # New Category (each stat has a : in the line)
            if ":" not in stripped:
                stats[stripped] = {}
                category = stripped
                continue

            name, value = stripped.split(": ")
            name = name.replace(" ", "-")
            value = self.try_int(value)

            stats[category][name] = value

        return stats

    def parse(self):
        stats = {}
        stubs = self.page.find_all(class_="stub")

        for stub in stubs:
            stub_stats = self.parse_stub(stub)
            stats.update(stub_stats)

        return stats
