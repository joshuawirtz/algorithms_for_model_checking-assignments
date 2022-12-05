class LabeledTransitionSystem:
    def __init__(self, states, action_labels, init_states, transitions):
        self.states = states
        self.action_labels = action_labels
        self.init_states = init_states
        self.transitions = transitions # \in S^3

    def box(self, s, al):
        al_not_predecessors = {ts for (ts, tal, te) in self.transitions if tal == al and te not in s}
        return self.states - al_not_predecessors

    def __repr__(self):
        return {"states": self.states,
                "action_labels": self.action_labels,
                "init_states": self.init_states,
                "transitions": self.transitions}.__repr__()