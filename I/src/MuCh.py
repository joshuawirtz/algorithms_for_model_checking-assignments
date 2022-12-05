import argparse
from enum import Enum
import logging
from logging import info
from os import path

from parsing.Parser import Parser

class Algorithm(Enum):
    NAIVE = 1
    EMERSON_LEI = 2

class MuCh():
    def __init__(self, algorithm, system_path, formula_path):
        self.algorithm = algorithm
        self.system_path = system_path
        self.formula_path = formula_path

    def parse(self):
        parser = Parser(self.system_path, self.formula_path)
        
        info("Parsing labelled transition system from '%s'.." % self.system_path)
        self.sysetm = parser.parse_system()
        info("Finished parsing of lablled transition system.")

        info("Parsing formula from '%s'.." % self.formula_path)
        self.formula = parser.parse_formula()
        info("Finished parsing of formula.")

    def check(self):
        if(self.algorithm == Algorithm.NAIVE):
           pass
        if(self.algorithm == Algorithm.EMERSON_LEI):
           pass


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
        algorithm = Algorithm[args.algorithm.upper()]

        system_path = args.system
        if(not path.exists(system_path)):
            raise ValueError("No such path %s." % system_path)

        formula_path = args.formula
        if(not path.exists(formula_path)):
            raise ValueError("No such path %s." % formula_path)

    except KeyError:
        raise ValueError("No such algorithm: %s. Choose one of %s." % (args.algorithm, [a.name for a in Algorithm]))

    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

    much = MuCh(algorithm, system_path, formula_path)
    much.parse()

if __name__ == "__main__":
    main()
    