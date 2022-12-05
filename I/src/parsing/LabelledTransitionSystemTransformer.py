from lark.visitors import Transformer

from LabeledTransitionSystem import LabeledTransitionSystem

class LabelledTransitionSystemTransformer(Transformer):
    def string(self, s):
        return s[1:-1]
    
    number = int

    FIRST_STATE = number
    NR_OF_TRANSITIONS = number
    NR_OF_STATES = number

    def aut_header(self, header):
        init_state, _, n_states = header
        return [set(range(n_states)), {init_state}]

    START_STATE = number
    LABEL = string
    END_STATE = number

    def aut_edge(self, transition):
        return tuple(transition)

    # args is a list containing (in this order)
    # set of states, initial_states and then transitions.
    # Order is always given, since all files start with aut_header
    # and then go on to specify transitions.
    def start(self, args):
        args = args[0] + args[1:]
        lts = LabeledTransitionSystem(*args)
        return lts