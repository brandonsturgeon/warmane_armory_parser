from parser.armory import ArmoryParser


class CharacterKillsParser(ArmoryParser):
    def get_section(self, soup):
        return soup.find(class_="pvpbasic")

    def parse_stub(self, stub):
        # 'total kills\n                    1387'
        stub_text = stub.text.strip().lower()

        # ['total kills', '                    1387']
        name, value = stub_text.split("\n")

        # 'total-kills'
        name = name.replace(" ", "-")

        # '1387'
        value = value.strip()

        # 1387
        value = self.try_int(value)

        return {name: value}

    def parse(self):
        kill_data = {}
        pvp_stubs = self.page.find_all(class_="stub")

        for stub in pvp_stubs:
            stub_data = self.parse_stub(stub)
            kill_data.update(stub_data)

        return kill_data
