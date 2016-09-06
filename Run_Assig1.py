#!/usr/bin/python
import fileinput

"""
Obatola Seward-Evans
CS 4341 Assignment 1
September 9th, 2016
"""
#This variable tells us whetehr we should use a greedy or iterative approach
method = ""
#This is our bas number we will operate on
base = 0
#This is the total time we are allowed to execute for
fp = fileinput.input("test_input1.txt"); 
with open("test_input1.txt") as file:
    method = file.readline().strip()
    base = file.readline().strip()

    print method
    print base
