import argparse
import logging
from logging import info
from os import path

import parsing.Parser as Parser
import checking.Checker as Checker

class MuCh():
    def __init__(self, algorithm, system_path, formula_path):
        self.algorithm = algorithm
        self.system_path = system_path
        self.formula_path = formula_path

    def parse(self):
        info("Parsing labelled transition system from '%s'.." % self.system_path)
        self.system = Parser.parse_system(self.system_path)
        info("Finished parsing of lablled transition system.")

        info("Parsing formula from '%s'.." % self.formula_path)
        self.formula = Parser.parse_formula(self.formula_path)
        info("Finished parsing of formula.")

    def check(self):
        Checker.solver(self.system, self.formula, self.algorithm)


def main():
    parser = argparse.ArgumentParser(description = "MuCh: A model checker for the modal mu-calculus.")

    parser.add_argument("algorithm", type=str,
                        help="Algorithm to be used for checking. One of naive, emerson_lei.")


    parser.add_argument("system", type=str,
                        help="File contaning labelled transition system in Aldebaran syntax.")

    parser.add_argument("formula", type=str,
                        help="File containing mu-calculus formula to be checked.")

    args = parser.parse_args()
    
    try:
        algorithm = Checker.Algorithm[args.algorithm.upper()]

        system_path = args.system
        if(not path.exists(system_path)):
            raise ValueError("No such path %s." % system_path)

        formula_path = args.formula
        if(not path.exists(formula_path)):
            raise ValueError("No such path %s." % formula_path)

    except KeyError:
        raise ValueError("No such algorithm: %s. Choose one of %s." % (args.algorithm, [a.name for a in Checker.Algorithm]))

    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

    much = MuCh(algorithm, system_path, formula_path)
    much.parse()
    much.check()

if __name__ == "__main__":
    main()
    