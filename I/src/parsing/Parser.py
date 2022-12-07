from lark import Lark
from LabeledTransitionSystem import LabeledTransitionSystem
from parsing.LabelledTransitionSystemTransformer import LabelledTransitionSystemTransformer
from parsing.FormulaTransformer import FormulaTransformer

import os

grammars_dir = os.path.join(os.path.dirname(__file__), 'grammars')

def parse_system(system_path):
    aut_parser = Lark.open(os.path.join(grammars_dir, 'aut.lark'), parser="lalr")
        
    system = aut_parser.parse(open(system_path).read())
        
    lts = LabelledTransitionSystemTransformer().transform(system)

    return lts

def parse_formula(formula_path):
    mcf_parser = Lark.open(os.path.join(grammars_dir, 'mcf.lark'), parser="lalr")

    formula = mcf_parser.parse(open(formula_path).read())

    mu = FormulaTransformer().transform(formula)
    
    return mu