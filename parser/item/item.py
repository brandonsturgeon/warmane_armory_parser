from parser.armory import ArmoryParser

class ItemParser(ArmoryParser):
    def get_section(self, soup):
        return soup.a

    def parse(self):
        # ['item=51543&ench=3842&gems=3642:3532:0']
        rel = self.page.get("rel", [])

        # Ignoring some garbage tags
        if len(rel) == 0:
            return

        # 'item=51543&ench=3842&gems=3642:3532:0'
        rel = rel[0]

        # ['item=51543', 'ench=3842', 'gems=3642:3532:0']
        rel = rel.split("&")

        # [['item', '51543'], ['ench', '3842'], ['gems', '3642:3532:0']]
        rel = [x.split("=") for x in rel]

        # {'item': '51543', 'ench': '3842', 'gems': '3642:3532:0'}
        return dict(rel)
