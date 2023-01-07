from ParityGame import *

def solve_game(game, lifting_order):
    """
    Solves a parity game using the small progress measures algorithm
    """

    # Find maximal priority of any vertex
    max_priority = max([v.priority for v in game.vertices])

    # T is defined to be larger than all other tuples (since for progress measure the value at index 0 is always 0)
    T = [1]

    # Initialize the dictionary mapping vertices to progress measures
    M = {}
    for v in game.vertices:
        M[v.identifier] = [0]*(max_priority + 1)

    # For each priority compute the number of vertices with that priority
    vertices_p = [0 for _ in range(max_priority + 1)]
    for v in game.vertices:
        vertices_p[v.priority] += 1

    def lift(vertex):
        """
        Auxiliary function used for lifting a vertex of a parity game

        Returns True if lifting was possible, False otherwise
        """

        def prog(v, w_id):
            """
            The prog function as defined in the lecture
            """

            # If the progress measure of w is T, v will become T
            if M[w_id] == T:
                return T

            m = [0]*(max_priority+1)

            # Priority of v is even
            if v.priority % 2 == 0:
                for i in range(v.priority + 1):
                    m[i] = M[w_id][i]
            # Priority of v is odd
            else:
                for i in reversed(range(1, v.priority + 1, 2)):
                    if M[w_id][i] < vertices_p[i]:
                        m[i] = M[w_id][i] + 1
                        for j in range(i):
                            m[j] = M[w_id][j]
                        break 
                    elif i == 1:
                        m = T
            return m

        if vertex.owner == Owner.EVEN:
            lifted_m = min([prog(vertex, w) for w in v.successors])
        else:
            lifted_m = max([prog(vertex, w) for w in v.successors])
        if lifted_m != M[v.identifier]:
            M[v.identifier] = lifted_m
            return True
        else:
            return False

    # Keep lifting vertices untill a fixpoint has been reached
    did_lift_vertex = True
    while did_lift_vertex:
        did_lift_vertex = False
        for v in lifting_order:
            did_lift_vertex = did_lift_vertex or lift(v)

    return {"even": {v for v in M if M[v] != T}, "odd": {v for v in M if M[v] == T}}

