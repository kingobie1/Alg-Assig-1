#!/usr/bin/python
"""
Obatola Seward-Evans, Dimitar Vouldjef, Frank Egan, Himanjal Sharma
CS 4341 Assignment 1
September 9th, 2016

This file requires Functions.py which holds the iterative deepending
and greedy seach functions.
"""
# import the actual functions from Functions.py:
import Functions
import Genetics
from collections import namedtuple
import sys

# File name that we will run our program with
fileName = sys.argv[1]

# This variable tells us whetehr we should use a greedy or iterative approach
method = ""

# This is our bas number we will operate on
base = 0

# This is our target number we will try to find
target = 0

# This is the total time we are allowed to execute for
time = 0

# Array of Operation holds all of the possible OperationStructs
ArrayOfOperations = []

# Operation structs hold individual tuples such as (+, 2) or (/, 3)
OperationStruct = namedtuple("OperationStruct", 'operator value')

# Open our file and start reading it 'with' takes care of closing
with open(fileName) as file:
    arrayLength = 0
    method = file.readline().strip()
    base = file.readline().strip()
    target = file.readline().strip()
    time = file.readline().strip()

    print "method:" + method
    print "base:" + base
    print "target:" + target
    print "time:" + time

    for line in file:
        arrayLength += 1
        # gets the operator and number (any number of digits) from the line
        # creates an OperationStruct from it and adds it to ArrayOfOperations
    	ArrayOfOperations.append(OperationStruct(operator = line[0], value = int(line.split()[1])))
    # print ArrayOfOperations

if method == "iterative":
    print "running iterative"
    path, elapsed, numExpanded, maxDepth = Functions.iterativeDeepening(int(base), ArrayOfOperations, int(target), float(time))
    path = path[::-1]
elif method == "genetic":
    print "running genetic"
    path, elapsed, numExpanded, maxDepth = Genetics.geneticSearch(base, ArrayOfOperations, target, time)
else:
    print "running greedy"
    path, elapsed, numExpanded, maxDepth = Functions.greedySearch(int(base), ArrayOfOperations, int(target), float(time))

for op in path:
    if op[1] != None:
        print str(op[0]) + " " + str(op[1].operator) + " " + str(op[1].value) + " = " + str(op[2])

print ''
print "Error: " + str(abs(int(target) - path[len(path)-1][2]))
print "Number of steps required: " + str(len(path))
print "Search required: " + str(elapsed) + " seconds"
print "Nodes expanded: " + str(numExpanded)
print "Maximum search depth: " + str(maxDepth)
print ''
print ''
