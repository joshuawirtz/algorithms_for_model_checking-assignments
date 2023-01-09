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

