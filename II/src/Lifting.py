import random

class Lifting:

    def __init__(self, game):
        self.game = game
    

class InputLifting(Lifting):

    def __iter__(self):
        return iter(self.game.vertices)

class RandomLifting(Lifting):

    def __iter__(self):
        shuffled = random.sample(self.game.vertices,
                                  len(self.game.vertices))
        return iter(shuffled)

class SuccessorLifting(Lifting):

    def __init__(self, game):
        super().__init__(game)
        successors = {v.identifier: 0 for v in self.game.vertices}
        for v in self.game.vertices:
            for s in v.successors:
                successors[s] += 1
        self.succesors = successors

    def __iter__(self):
        return iter(sorted(self.game.vertices, key=lambda v: self.succesors[v.identifier]))

# First lift the vertices with selfloops
