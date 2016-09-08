"""
Obatola Seward-Evans, Dimitar Vouldjef, Frank Egan, Himanjal Sharma
CS 4341 Assignment 1
September 9th, 2016

This file holds the functions used in Run_Assig1.py
"""

# - - - "ITERATIVE DEEPENING" FUNCTION - - -
#This our function for doing an Iterative Depth First Search
#(inspired by https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search)
def iterativeDeepening(start, operations, goal):
    depth = 0
    solution = []
    while solution == None or len(solution) == 0:
        solution = depthLimited(start, operations, goal, depth)
        depth = depth + 1
    return solution, depth

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

def depthLimited(start, operations, goal, depth):
    if depth == 0 and start == goal:
        return [start]
    elif depth > 0:
        for nextOp in operations:
        	child = operateOn(start, nextOp)
        	found = depthLimited(child, operations, goal, depth-1)
        	if found != None and len(found) > 0:
				found.append(start)
				return found
	return None

# - - - "GREEDY SEARCH" FUNCTION - - -
def greedySearch(start, operations, goal):
    print ("I will do a greedy Search!")
    return