import random

class Lifting:

    def __init__(self, game):
        self.game = game
    

class InputLifting(Lifting):

    def __iter__(self):
        return iter(self.game.vertices)

class RandomLifting(Lifting):

    def __init__(self, game, seed):
        super().__init__(game)
        self.seed = seed

    def __iter__(self):
        random.seed(self.seed)
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

class SelfLoopLifting(self):

    def __init__(self, game):
        super().__init__(game)
        self.self_loops = [v for v in game.vertices if v.identifier in v.succesors]
        self.no_self_loops = [v for v in game.vertices if v.identifier not in v.succesors]

    def __iter__(self):
        return iter(self_loops + no_self_loops)
