from lark import Lark
from LabeledTransitionSystem import LabeledTransitionSystem
from parsing.LabelledTransitionSystemTransformer import LabelledTransitionSystemTransformer

class Parser():
    def __init__(self, system_path, formula_path):
        self.system_path = system_path
        self.formula_path = formula_path

    def parse_system(self):
        aut_parser = Lark.open("grammars/aut.lark", parser="lalr")
        
        system = aut_parser.parse(open(self.system_path).read())
        
        lts = LabelledTransitionSystemTransformer().transform(system)

        return lts

    def parse_formula(self):
        mcf_parser = Lark.open("grammars/mcf.lark", parser="lalr")

        formula = mcf_parser.parse(open(self.formula_path).read())

        pass