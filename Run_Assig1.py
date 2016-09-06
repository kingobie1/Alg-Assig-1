#!/usr/bin/python

"""
Obatola Seward-Evans
CS 4341 Assignment 1
September 9th, 2016
"""
#This variable tells us whetehr we should use a greedy or iterative approach
method = ""
#This is our bas number we will operate on
base = 0
#This is our target number we will try to find
target = 0
#This is the total time we are allowed to execute for
time = 0

#Open our file and start reading it with takes care of closing
with open("test_input1.txt") as file:
    method = file.readline().strip()
    base = file.readline().strip()
    target = file.readline().strip()
    time = file.readline().strip()

    for line in file:
    	print line

    print method
    print base
    print target
    print time
