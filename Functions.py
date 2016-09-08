"""
Obatola Seward-Evans, Dimitar Vouldjef, Frank Egan, Himanjal Sharma
CS 4341 Assignment 1
September 9th, 2016

This file holds the functions used in Run_Assig1.py
"""


# Limit execution time from StackOverflow
# http://stackoverflow.com/questions/366682/how-to-limit-execution-time-of-a-function-call-in-python
from __future__ import with_statement
import signal
from contextlib import contextmanager
import time

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
					return solution, (time.time() - init_time)

				depth = depth + 1
	except TimeoutException:
	    return solution, (time.time() - init_time)

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


def greedySearch(start, operations, goal, arrayLength):
    print ("I will do a greedy Search!")
    num = 0
    count = 0
    smallestSum = start

    while operations:
        for num in range(0, arrayLength):
            operateOn(smallestSum, operations[num][1][0])
            # del operations[0]   
            count += 1

    
    return

# produces the absolute difference between the value and the goal
def difference (value, goal):
    return abs(value - goal)
