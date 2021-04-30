from parser.character.kills import CharacterKillsParser


class CharacterProfessionsParser(CharacterKillsParser):
    def get_section(self, soup):
        return soup.find(class_="profskills")

    def format_prof(self, value):
        value = value.split(" / ")[0]
        value = self.try_int(value)

        return value

    def parse(self):
        prof_data = super().parse()
        return {k: self.format_prof(v) for k, v in prof_data.items()}
