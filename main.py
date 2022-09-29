import json
from armory_parser import parse_character

character = "Moot"
realm = "Icecrown"

data = parse_character(character, realm)
print(json.dumps(json.loads(data.to_json()), indent=4))
