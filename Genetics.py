import numpy as np
import random
import Functions
import time
import copy
"""
Obatola Seward-Evans, Dimitar Vouldjef, Frank Egan, Himanjal Sharma
CS 4341

This file contains functions and classes used for encoding problems
as organisms that will be bred and selected for that find optial solutions
"""

NUMOPS = 5
INITIAL_ORGANISM_SIZE = 5
INITIAL_POPULATION_SIZE = 5
KEEP_BEST = 1
CROSSOVER_BEST = 2
LENGTH_PENALTY = 0.2

# amount we want the program to stop at
FITNESS_THRESHOLD = 0

def geneticSearch(start, operations, goal, max_exec):
	"""
	Repeats until found or time is up
		- getFitness -
		- crossover on best fitnesses -
		get collection of  crossed over organisms
		mutate

	Returns:
		error (int): The amount our final answer is off by.
		size (int): Size of our best organism.
		population (int): Size of our final population.
		gens (int): The number of generation it took solve the problem.
	"""

	# create initial population
	population = populate(INITIAL_POPULATION_SIZE, len(operations))
	count = 0

	population = sortPopulation(population, start, operations, goal)
	best = population[0]

	init_time = time.time()
	try:
		with Functions.max_time(max_exec):

			# Repeat until gett fitness under 10.0
			while best.getFitness(start, operations, goal) > FITNESS_THRESHOLD: #and count < MAX_DEPTH:

				newPopulation = copy.deepcopy(population[0:KEEP_BEST])

				for i in range(CROSSOVER_BEST - 1):
					organism1, organism2 = population[i].crossover(population[i + 1])
					organism1.mutate()
					organism2.mutate()
					newPopulation.append(organism1)
					newPopulation.append(organism2)

				population = sortPopulation(newPopulation, start, operations, goal)
				print "Population = " + str(population)
				best = population[0]

				count += 1

			# TODO: give correct return
			return (best.toPath(start, operations), (time.time() - init_time), len(population), count)

	except Functions.TimeoutException:
		return (best.toPath(start, operations), (time.time() - init_time), len(population), count)


def sortPopulation(population, start, operations, goal):
	return sorted(population, key=lambda o: o.getFitness(start, operations, goal))

def populate(initSize, numOps):
	population = []
	for i in xrange(initSize):
		population.append(Organism(numOps))
	return population

# Utility function for fitness
def fitnessUtility(lengthOfOrganism):
	# penalize longer organisms
	return lengthOfOrganism * LENGTH_PENALTY


class Organism:
	"""An Organism represents an encoding of a solution within it's chromosome"""

	# This is an encoding for the solution into an organism
	# each number is an index into the operators we read in.
	chromosome = []
	# The number of operators that we read in, it's used to
	# encode and mutate organisms
	numOps = 0

	def __init__(self, numOps, geneSeq=None):
		self.numOps = numOps
		if geneSeq == None:
			self.chromosome = np.random.randint(low=0, high=numOps-1, size=INITIAL_ORGANISM_SIZE).tolist()
		else:
			self.chromosome = geneSeq

	def __repr__(self):
		return str(self.chromosome)
		
	def getChromosome(self):
		return self.chromosome

	def getLen(self):
		return len(self.chromosome)

	# Defines the organisms fitness given the operations and starting base number.
	# Args:
	# 	base (float): The starting number we read.
	# 	ops (OperationStruct[]): An array of operations we read form config file.
	# 	goal (float): The desired goal of base after operations.
	# Returns:
	# 	How close the organism is to the desired value once decoded.
	def getFitness(self, base, ops, goal):

		product = self.operate(base, ops)
		difference = Functions.diff(product, goal)
		fitness = difference + fitnessUtility(self.getLen())
		return fitness

	def getDiff(self, base, ops, goal):

		product = self.operate(base, ops)
		difference = Functions.diff(product, goal)
		return difference

	
	# Mutates the organism either by adding, subtracting or modifyinh a gene.
	# Args:
	# 	prob (float): The probability that we will actually mutate. Values of 1 is certain 0 is never.
	def mutate(self):

		# Do mutation
		mType = random.randint(1, 3)

		if mType == 1:
			# We are adding a gene as an encoded index
			op = random.randint(0, self.numOps-1)
			self.chromosome.append(op)
		elif mType == 2:
			# We are removing genes unless there is only one left
			if len(self.chromosome) != 1:
				i = random.randint(0, len(self.chromosome)-1)
				self.chromosome.pop(i)

		elif mType == 3:
			# We are modigying a gene
			i = random.randint(0, len(self.chromosome)-1)
			self.chromosome[i] = random.randint(0, self.numOps-1)

	def crossover(self, otherOrganism):
		primary = None
		secondary = None
		if self.getLen() < otherOrganism.getLen():
			primary = self.getChromosome()
			secondary = otherOrganism.getChromosome()
		else:
			primary = otherOrganism.getChromosome()
			secondary = self.getChromosome()

		cuttingPoint = random.randint(0, len(primary) - 1)
		#print "... cutting point: " + str(cuttingPoint)
		#print ".."

		sectionA1 = primary[0:cuttingPoint]
		sectionA2 = secondary[cuttingPoint:(len(secondary))]
		sectionB1 = secondary[0:cuttingPoint]
		sectionB2 = primary[cuttingPoint:(len(primary))]

		newOrganismGene1 = sectionA1 +sectionA2
		newOrganismGene2 = sectionB1 + sectionB2

		return (Organism(self.numOps, geneSeq=newOrganismGene1), Organism(self.numOps, geneSeq=newOrganismGene2))

	# Goes through each encoded operation in the chromosome and applies that to the base.

	# Args:
	# 	start (int): The base number form our config file.
	# 	ops (OperationStruct[]): An array of operations we read from config file.
	def operate(self, base, ops):

		total = base
		for index in self.chromosome:
			op = ops[index]
			temp = Functions.operateOn(total, op)
			total = temp
		return total

	def toPath(self, base, ops):
		""" 
		Creates a matrix where each row is the base for that operation,
			the operation applied to it and the product of that operation.
		Args:
			base (float): Starting point form input file.
			ops (OperationStruct[]): The operations available to us.

		Return: 
			[[float, OperationStruct, float]]
		"""
		path = []
		#Iterate through chromosome and apply operation
		for i in self.chromosome:
			#This loop's operation
			op = ops[i]
			nextBase = Functions.operateOn(base, op)
			path.append([base, op, nextBase])
			base = nextBase
		return path






