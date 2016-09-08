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
	best = None
	while best == None or best > 0:
		temp = depthLimited(start, operations, goal, depth)

		if best == None or temp[0][0] < best:
			best = temp[0][0]
			solution = temp

		if best == 0:
			return solution

		depth = depth + 1

def operateOn(start, operation):
	if operation.operator == "+":
		return int(start + operation.value)
	elif operation.operator == "-":
		return int(start - operation.value)
	elif operation.operator == "*":
		return int(start * operation.value)
	elif operation.operator == "/":
		return int(start / operation.value)
	elif operation.operator == "^":
		return int(start ** operation.value)

def depthLimited(start, operations, goal, depth):
	if depth == 0:
		return [(abs(goal - start), None, None)]
	elif depth > 0:
		minimum = None
		path = None
		for nextOp in operations:
			child = operateOn(start, nextOp)
			found = depthLimited(child, operations, goal, depth-1)
			if minimum == None or found[0][0] < minimum:
				minimum = found[0][0]
				found.append((start, nextOp, child))
				path = found
		return path

# - - - "GREEDY SEARCH" FUNCTION - - -
def greedySearch(start, operations, goal):
	print ("I will do a greedy Search!")

	print start
	print goal
	
	return