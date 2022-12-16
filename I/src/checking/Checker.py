from enum import Enum
import logging

def reduce_formula(formula_tree, reduceFixPoints=True):
    """Reduces the input parsing tree formula_tree by traversing it from top to bottom.

    The following reductions will be applied:
     - False is replaced with !True
     - <a>f is replaced with ![a]!f
    And if input parameter reduceFixPoints == True:
     - mu X. f is replaced with !nu X. !f[X := !X]
    """

    operand = list(formula_tree.keys())[0]
    arguments = formula_tree[operand]
    
    def negate_variable(tree, x):
        """
        Traverses tree down to leaves and replaces any occurences of variable x with !x
        """
        operand = list(tree.keys())[0]
        arguments = tree[operand]
        
        if operand == "var":
            if arguments == x["var"]:
                return {"neg": tree}
            else:
                return tree
        elif operand == "val":
            return tree
        elif operand == "and" or operand == "or":
            return {operand: [negate_variable(arg, x) for arg in arguments]}
        elif operand == "box" or operand == "diamond":
            return {operand: [arguments[0], negate_variable(arguments[1], x)]}
        elif operand == "mu" or operand == "nu":
            var = arguments[0]
            form = arguments[1]
            return {operand: [var, negate_variable(form, x)]}
        else:
            return {operand: negate_variable(arguments, x)}

    if operand == "val":
        if arguments == False:
            return {"neg": {"val": True}}
        else:
            return formula_tree
    elif operand == "var":
        return formula_tree
    elif operand == "diamond":
        return {"neg": {"box": [arguments[0], {"neg": reduce_formula(arguments[1], reduceFixPoints)}]}}
    elif operand == "box":
        return {"box": [arguments[0], reduce_formula(arguments[1], reduceFixPoints)]}
    elif operand == "and" or operand == "or":
        return {operand: [reduce_formula(arg, reduceFixPoints) for arg in arguments]}
    elif operand == "mu":
        var = arguments[0]
        form = arguments[1]
        if reduceFixPoints:
            return {"neg": {"nu": [var, {"neg": reduce_formula(negate_variable(form, var), reduceFixPoints)}]}}
        else:
            return {operand: [var, reduce_formula(form, reduceFixPoints)]}
    elif operand == "nu":
        var = arguments[0]
        form = arguments[1]
        return {operand: [var, reduce_formula(form, reduceFixPoints)]}
    else:
        return {operand: reduce_formula(arguments, reduceFixPoints)}


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
        states = naive(lts,reduce_formula(formula))
    elif algorithm == Algorithm.EMERSON_LEI:
        states = emmerson_lei(lts,reduce_formula(formula,False))
    else:
        raise ValueError("Algorithm %s is unsupported." % algorithm.name)
    return (0 in states, states, counter)
    

def naive(lts, formula):
    global counter
    states = lts.states
    operand = list(formula.keys())[0]
    arguments = formula[operand]
    if operand == "neg":
        return states - (naive(lts,arguments))
    elif operand == "or":
        return naive(lts,arguments[0]) | naive(lts,arguments[1])
    elif operand == "and":
        return naive(lts,arguments[0]) & naive(lts,arguments[1])
    elif operand == "box":
        return lts.box(naive(lts,arguments[1]),arguments[0])
    elif operand == "val":
        return states
    elif operand == "var":
        return variables[arguments] 
    elif operand == "nu":
        variable = arguments[0]["var"]
        #we start with all the states
        variables[variable] = states
        counter += 1
        newSol = naive(lts,arguments[1])
        while newSol != variables[variable]:
            counter += 1
            variables[variable] = newSol
            newSol = naive(lts,arguments[1])            
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