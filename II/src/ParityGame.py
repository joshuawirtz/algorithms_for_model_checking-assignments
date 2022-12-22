from enum import Enum

class ParityGame:

    def __init__(self, vertices):
        self.vertices = vertices

    def __repr__(self):
        return {"vertices": self.vertices}.__repr__()

class Order(Enum):
    INPUT = 1
    RANDOM = 2
        
class Vertex:

    def __init__(self, identifier, priority, owner, successors, name):
        self.identifier = identifier
        self.priority = priority
        self.owner = owner
        self.successors = successors
        self.name = name

    def __repr__(self):
        return {"identifier": self.identifier,
                "priority:": self.priority,
                "owner": self.owner,
                "successors": self.successors,
                "name": self.name}.__repr__()

class Owner(Enum):
    EVEN = 0
    ODD = 1