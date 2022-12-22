from lark.visitors import Transformer

from ParityGame import *

class ParityGameTransformer(Transformer):
    def string(self, s):
        return s[1:-1]

    number = int
    
    def owner(self, o):
        (o,) = o
        return Owner(int(o))

    IDENTIFIER = number
    PRIORITY = number
    OWNER = owner

    NAME = string

    successors = list

    def node_spec(self, spec):
        return Vertex(*spec)

    def start(self, game):
        return ParityGame(game[1:])