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

#inspired by http://webdocs.cs.ualberta.ca/~jonathan/PREVIOUS/Courses/657/Notes/10.Single-agentSearch.pdf
def ida_star(start, operations, goal):
    thresh = 0
    solution = None
    while solution == None:
        solution = threshLimited(start, operations, goal, 0, thresh)
        thresh = thresh + 1
    return solution

def threshLimited(start, operations, goal, cost, thresh):
    print "start:" + str(start)
    f = cost + 0
    if f > thresh:
        return None
    if start == goal:
        return start
    elif f >= 0:
        for nextOp in operations:
            child = operateOn(start, nextOp)
            found = threshLimited(child, operations, goal, cost + 1, thresh)
            if found != None:
                return found
    return None

# - - - "GREEDY SEARCH" FUNCTION - - -
def greedySearch(start, operations, goal):
    print ("I will do a greedy Search!")
    return