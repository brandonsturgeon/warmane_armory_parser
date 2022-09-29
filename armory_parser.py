from parser.character.character import CharacterParser


def parse_character(name, realm="Icecrown"):
    return CharacterParser(name).build_character()
