from parser.character.kills import CharacterKillsParser

class CharacterSpecializationParser(CharacterKillsParser):
    SPEC_ORDER = ["primary", "secondary"]

    def get_section(self, soup):
        return soup.find(class_="specialization")

    def parse_stub(self, stub):
        name = stub.find(class_="text")
        name = name.find(text=True)
        name = name.strip().lower()

        value = stub.find(class_="value").text

        return {
            "name": name,
            "points": value
        }

    def parse(self):
        spec_data = {}
        spec_stubs = self.page.find_all(class_="stub")

        for which, stub in zip(self.SPEC_ORDER, spec_stubs):
            stub_data = self.parse_stub(stub)
            spec_data.update({which: stub_data})

        return spec_data
