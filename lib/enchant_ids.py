import json

LOOKUP = {}
REVERSE_LOOKUP = {}

with open("lib/data/enchant_ids.json", "rb") as enchant_ids:
    LOOKUP = json.loads(enchant_ids.read())

REVERSE_LOOKUP = {v.lower(): k for k, v in LOOKUP.items()}


class EnchantIDs:
    def __init__(self):
        self.lookup = LOOKUP
        self.reverse_lookup = REVERSE_LOOKUP

    def get(self, enchant_id: str):
        return self.lookup.get(enchant_id)

    def get_by_name(self, enchant_name: str):
        return self.reverse_lookup.get(enchant_name.lower())
