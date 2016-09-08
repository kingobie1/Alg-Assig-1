"""
Obatola Seward-Evans, Dimitar Vouldjef, Frank Egan, Himanjal Sharma
CS 4341 Assignment 1
September 9th, 2016

This file holds the functions used in Main.py
"""
import sys
# - - - "ITERATIVE DEEPENING" FUNCTION - - -
#This our function for doing an Iterative Depth First Search
#(inspired by https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search)
def iterativeDeepening(start, operations, goal):
    depth = 0
    solution = None
    while solution == None:
        path = [] # <-- Empty List
        solution = depthLimited(start, operations, goal, depth, path)
        depth = depth + 1
    return solution

def operateOn(start, operation):
    if operation.operator == "+":
        return start + operation.value
    elif operation.operator == "-":
        return start - operation.value
    elif operation.operator == "*":
        return start * operation.value
    elif operation.operator == "/":
        return start / operation.value
    elif operation.operator == "^":
        return start ** operation.value

# def depthLimited(start, operations, goal, depth, path):
#     print "start:" + str(start)

#     if depth == 0 and start == goal:
#         return start
#     elif depth > 0:
#         for nextOp in operations:
#             child = operateOn(start, nextOp)
#             found = depthLimited(child, operations, goal, depth-1, path)
#             if found != None:
#                 return found
#     return None
def depthLimited(start, operations, goal, depth, path):
    print "start:" + str(start)

    if depth == 0 and start == goal:
        return start
    elif depth > 0:
        for nextOp in operations:
            child = operateOn(start, nextOp)
            found = depthLimited(child, operations, goal, depth-1, path)
            if found != None:
                return found
    return None

def ida_star(start, operations, goal):
    depth = 0
    bound = abs(goal - start)
    solution = None
    while solution == None:
        solution = search(start, depth, operations, goal, 0)
        if solution == goal:
            return solution
        depth = depth + 1
        bound = solution
    return solution
 
def search(start, cost, operations, goal, bound):
    h = abs(goal - start)
    f = cost + h
    if f > bound:
       return None
    if start == goal:
        return goal
    min = sys.maxint
    for nextOp in operations:
        child = operateOn(start, nextOp)
        found = search(child, cost + 1, operations, goal, bound)
        print "Found:" + found
        if found == goal:
             return goal
        if found < min:
            min = found
    return min

# - - - "GREEDY SEARCH" FUNCTION - - -
def greedySearch(start, operations, goal):
    print ("I will do a greedy Search!")
    return