class ArmoryParser:
    def __init__(self, soup):
        self.soup = soup
        self.page = self.get_section(soup)

    def try_int(self, value):
        try:
            return int(value)
        except ValueError:
            return value

    def get_section(self, soup):
        return soup.find(id=self.content_id)

    def parse(self):
        raise NotImplementedError
