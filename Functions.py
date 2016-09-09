"""
Obatola Seward-Evans, Dimitar Vouldjef, Frank Egan, Himanjal Sharma
CS 4341 Assignment 1
September 9th, 2016

This file holds the functions used in Main.py
"""
# Limit execution time from StackOverflow
# http://stackoverflow.com/questions/366682/how-to-limit-execution-time-of-a-function-call-in-python
from __future__ import with_statement
import signal
from contextlib import contextmanager
import time
import sys

class TimeoutException(Exception): pass

@contextmanager
def max_time(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException
    signal.signal(signal.SIGALRM, signal_handler)
    signal.setitimer(signal.ITIMER_REAL, seconds)
    try:
        yield
    finally:
        signal.alarm(0)


# - - - "ITERATIVE DEEPENING" FUNCTION - - -
#This our function for doing an Iterative Depth First Search
#(inspired by https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search)
def iterativeDeepening(start, operations, goal, max_exec):
	depth = 0
	solution = []
	best = None

	init_time = time.time()
	try:
	    with max_time(max_exec):
	        while best == None or best > 0:
				temp = depthLimited(start, operations, goal, depth)

				if best == None or temp[0][0] < best:
					best = temp[0][0]
					solution = temp

				if best == 0:
					return solution[1::], (time.time() - init_time), expanded_nodes(depth, len(operations)), depth

				depth = depth + 1
	except TimeoutException:
	    return solution[1::], (time.time() - init_time), expanded_nodes(depth, len(operations)), depth

def expanded_nodes(depth, ops):
    result = 0
    while depth > 0:
        result += ops ** depth
        depth -= 1
    return result

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
def greedySearch(start, operations, goal, max_exec):
    bestSum = start
    path = []
    count = 0

    init_time = time.time()
    try:
        with max_time(max_exec):
            while diff(bestSum, goal) > 0:
                count += 1
                result = None
                extendPath = None
                for nextOp in operations:

                    temp = operateOn(bestSum, nextOp)
                    if result == None or diff(temp, goal) < diff(result, goal):
                        result = temp
                        extendPath = (bestSum, nextOp, temp)
                if diff(result, goal) < diff(bestSum, goal):
                    bestSum = result
                    path.append(extendPath)

                if diff(bestSum, goal) == 0:
                    return path, (time.time() - init_time), count * len(operations), count

    except TimeoutException:
        return path, (time.time() - init_time), count * len(operations), count

# produces the absolute diff between the value and the goal
def diff(value, goal):
    return abs(value - goal)






