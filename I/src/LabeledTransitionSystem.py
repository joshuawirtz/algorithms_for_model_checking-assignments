class LabeledTransitionSystem:
    def __init__(self, states, action_labels, init_states, transitions):
        self.states = states
        self.action_labels = action_labels
        self.init_states = init_states
        self.transitions = transitions # \in S^3

    def box(s,al):
        [te for (ts,tal,te) in self.transitions
            if ts in s and tal == al]

    def __repr__(self):
        return {"states": self.states,
                "action_labels": self.action_labels,
                "init_states": self.init_states,
                "transitions": self.transitions}.__repr__()