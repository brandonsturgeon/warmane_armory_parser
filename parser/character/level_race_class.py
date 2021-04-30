from parser.armory import ArmoryParser


class CharacterLevelRaceClassParser(ArmoryParser):
    def get_section(self, soup):
        return soup.find(class_="level-race-class")

    def parse(self):
        data = self.page.text
        data = data.strip()
        data = data.replace(",", "")
        data = data.lower()

        # ['level', '80', 'tauren', 'warrior', 'icecrown']
        data_spl = data.split()

        return {
            "level": self.try_int(data_spl[1]),
            "race": data_spl[2],
            "class": data_spl[3],
            "realm": data_spl[4]
        }
