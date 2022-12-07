from lark import Lark
from LabeledTransitionSystem import LabeledTransitionSystem
from parsing.LabelledTransitionSystemTransformer import LabelledTransitionSystemTransformer
from parsing.FormulaTransformer import FormulaTransformer

def parse_system(path):
    aut_parser = Lark.open("src/grammars/aut.lark", parser="lalr")
        
    system = aut_parser.parse(open(path).read())
        
    lts = LabelledTransitionSystemTransformer().transform(system)

    return lts

def parse_formula(path):
    mcf_parser = Lark.open("src/grammars/mcf.lark", parser="lalr")

    formula = mcf_parser.parse(open(path).read())

    mu = FormulaTransformer().transform(formula)
    
    return mu