from parser.armory import ArmoryParser


class CharacterActivityParser(ArmoryParser):
    def get_section(self, soup):
        return soup.find(class_="recent-activity")

    def extract_id(self, stub):
        # 'http://wotlk.cavernoftime.com/achievement=2157'
        href = stub.a.get("href")

        # ['http://wotlk.cavernoftime.com/achievement', '2157']
        spl = href.split("=")

        return spl[-1]

    def extract_name(self, stub):
        return stub.find(class_="name").text

    def extract_timing(self, stub):
        return stub.find(class_="time").text

    def parse_stub(self, stub):
        stub_id = self.extract_id(stub)
        name = self.extract_name(stub)
        timing = self.extract_timing(stub)

        return {
            stub_id: {
                "name": name,
                "when": timing
            }
        }

    def parse(self):
        activity_data = {}
        stubs = self.page.find_all(class_="stub")

        for stub in stubs:
            stub_data = self.parse_stub(stub)
            activity_data.update(stub_data)

        return activity_data
