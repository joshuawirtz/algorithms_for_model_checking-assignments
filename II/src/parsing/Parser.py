from pathlib import Path

from lark import Lark

from parsing.Transformers import ParityGameTransformer

grammars_dir = Path(__file__).parent.joinpath("grammars")

def parse_gm(path):
    gm_parser = Lark.open(grammars_dir.joinpath("gm.lark"), parser="lalr")

    gm = gm_parser.parse(path.open().read())

    game = ParityGameTransformer().transform(gm)

    return game