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
    method = file.readline().strip()
    base = file.readline().strip()
    target = file.readline().strip()
    time = file.readline().strip()

    print "method:" + method
    print "base:" + base
    print "target:" + target
    print "time:" + time

    for line in file:
        # gets the operator and number (any number of digits) from the line
        # creates an OperationStruct from it and adds it to ArrayOfOperations
    	ArrayOfOperations.append(OperationStruct(operator = line[0], value = int(line.split()[1])))
    # print ArrayOfOperations

path = Functions.iterativeDeepening(int(base), ArrayOfOperations, int(target))
for op in path[::-1]:
    if op[1] != None:
        print str(op[0]) + " " + str(op[1].operator) + " " + str(op[1].value) + " = " + str(op[2])
