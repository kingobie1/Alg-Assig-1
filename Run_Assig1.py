"""
Obatola Seward-Evans, Dimitar Vouldjef, Frank Egan, Himanjal Sharma
CS 4341 Assignment 1
September 9th, 2016

This file requires Functions.py which holds the iterative deepending
and greedy seach functions.
"""
#!/usr/bin/python

# import the actual functions from Functions.py:
from Functions import *
from collections import namedtuple

# Operation structs hold individual tuples such as (+, 2) or (/, 3)
OperationStruct = namedtuple('operation','value')

# Array of Operation holds all of the possible OperationStructs
ArrayOfOperations = []

iterativeDeepening(ArrayOfOperations)

