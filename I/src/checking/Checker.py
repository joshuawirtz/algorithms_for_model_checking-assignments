from enum import Enum

def reduceFormula(t, reduceFixPoints=True):
    operand = list(t.keys())[0]
    arguments = t[operand]

    def negate(t, x):
        o = list(t.keys())[0]
        a = t[o]

        if o == "var":
            if a == x["var"]:
                return {"neg": t}
            else:
                return t
        elif o == "val":
            return t
        elif o == "and" or o == "or":
            return {o: [negate(arg, x) for arg in a]}
        elif o == "box" or o == "diamond":
            return {o: [a[0], negate(a[1], x)]}
        elif o == "mu" or o == "nu":
            v = arguments[0]
            f = arguments[1]
            return {o: [v, negate(f, x)]}
        else:
            return {o: negate(a, x)}

    if operand == "val":
        if arguments == False:
            return {"neg": {"val": True}}
        else:
            return t
    elif operand == "var":
        return t
    elif operand == "diamond":
        return {"neg": {"box": [arguments[0], {"neg": reduceFormula(arguments[1], reduceFixPoints)}]}}
    elif operand == "box":
        return {"box": [arguments[0], reduceFormula(arguments[1], reduceFixPoints)]}
    elif operand == "and" or operand == "or":
        return {operand: [reduceFormula(arg, reduceFixPoints) for arg in arguments]}
    elif operand == "mu":
        v = arguments[0]
        f = arguments[1]
        if reduceFixPoints:
            return {"neg": {"nu": [v, {"neg": reduceFormula(negate(f, v), reduceFixPoints)}]}}
        else:
            return {operand: [v, reduceFormula(f, reduceFixPoints)]}
    elif operand == "nu":
        v = arguments[0]
        f = arguments[1]
        return {operand: [v, reduceFormula(f, reduceFixPoints)]}
    else:
        return {operand: reduceFormula(arguments, reduceFixPoints)}

class Algorithm(Enum):
    NAIVE = 1
    EMERSON_LEI = 2

counter = 0
#use a dictoinary to keep track of the variables
variables = dict()  
# run solver with a lts a formula and the type of algorithm desired, True for naive
# false for emmerson_lei-lei
def solver(lts, formula, algorithm):
    global counter
    counter = 0
    if algorithm == Algorithm.NAIVE:
        states = simple(lts,reduceFormula(formula))
    elif algorithm == Algorithm.EMERSON_LEI:
        states = emmerson_lei(lts,reduceFormula(formula,False))
    else:
        raise ValueError("Algorithm %s is unsupported." % algorithm.name)
    print(0 in states)
    print(counter)
    #temp
    print(states)
    

def simple(lts, formula):
    global counter
    states = lts.states
    operand = list(formula.keys())[0]
    arguments = formula[operand]
    if operand == "neg":
        return states - (simple(lts,arguments))
    elif operand == "or":
        return simple(lts,arguments[0]) | simple(lts,arguments[1])
    elif operand == "and":
        return simple(lts,arguments[0]) & simple(lts,arguments[1])
    elif operand == "box":
        return lts.box(simple(lts,arguments[1]),arguments[0])
    elif operand == "val":
        return states
    elif operand == "var":
        return variables[arguments] 
    elif operand == "nu":
        variable = arguments[0]["var"]
        #we start with all the states
        if (type != "nu" or (not variable in variables)):
            variables[variable] = states
        counter = counter +1
        newSol = emmerson_lei(lts,arguments[1],"nu")
        while newSol != variables[variable]:
            counter += 1
            variables[variable] = newSol 
            newSol = emmerson_lei(lts,arguments[1],"nu")
        return newSol
    else:
        return states

def emmerson_lei(lts, formula,type = "null"):
    global counter
    states = lts.states
    operand = list(formula.keys())[0]
    arguments = formula[operand]
    if operand == "neg":
        return states - (emmerson_lei(lts,arguments,type))
    elif operand == "or":
        return emmerson_lei(lts,arguments[0],type) | emmerson_lei(lts,arguments[1],type)
    elif operand == "and":
        return emmerson_lei(lts,arguments[0],type) & emmerson_lei(lts,arguments[1],type)
    elif operand == "box":
        return lts.box(emmerson_lei(lts,arguments[1],type),arguments[0])
    elif operand == "val":
        return states
    elif operand == "var":
        return variables[arguments] 
    elif operand == "nu":
        variable = arguments[0]["var"]
        #we start with all the states
        if (type != "nu" or (not variable in variables)):
            variables[variable] = states
        counter += 1
        newSol = emmerson_lei(lts,arguments[1],"nu")
        while newSol != variables[variable]:
            counter += 1
            variables[variable] = newSol 
            newSol = emmerson_lei(lts,arguments[1],"nu")
        return newSol
    elif operand == "mu":
        variable = arguments[0]["var"]
        #we start with the empty set of states
        if (type != "mu" or (not variable in variables)):
            variables[variable] = set()
        counter += 1
        newSol = emmerson_lei(lts,arguments[1],"mu")
        while newSol != variables[variable]:
            counter += 1
            variables[variable] = newSol 
            newSol = emmerson_lei(lts,arguments[1],"mu")
        return newSol
    else:
        return states