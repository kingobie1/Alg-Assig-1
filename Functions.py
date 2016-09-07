"""
Obatola Seward-Evans, Dimitar Vouldjef, Frank Egan, Himanjal Sharma
CS 4341 Assignment 1
September 9th, 2016

This file holds the functions used in Run_Assig1.py
"""

# - - - "ITERATIVE DEEPENING" FUNCTION - - -
def iterativeDeepening(start, operations, goal):
    print ("I will do iterative deepening!")
    depth = 0
    solution = None
    while solution == None:
        visited = [] # <-- Empty List
        solution = depthLimited(start, operations, goal, depth, visited)
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

def depthLimited(start, operations, goal, depth, visited):
    if depth == 0 and start == goal:
        return start
    elif depth > 0:
        for nextOp in operations:
        	child = operateOn(start, nextOp)
        	visited = depthLimited(child, operations, goal, depth-1, visited)
        	if visited != None:
				return visited
	return None

# - - - "GREEDY SEARCH" FUNCTION - - -
def greedySearch(listOfOperations):
    print ("I will do a greedy Search!")
    return