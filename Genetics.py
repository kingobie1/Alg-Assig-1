import numpy as np
import random
import Functions
"""
Obatola Seward-Evans, Dimitar Vouldjef, Frank Egan, Himanjal Sharma
CS 4341

This file contains functions and classes used for encoding problems
as organisms that will be bred and selected fo rthat find optial solutions
"""

NUMOPS = 5
INITIAL_ORGANISM_SIZE = 5
INITIAL_POPULATION_SIZE = 10
MUTATEPROB = 0.11

def geneticSearch(start, operations, goal, max_exec):
	"""
	Returns:
		[int, OperationStruct, int] The solution path we took to solve,
		int	Execution time,
		int	Expanded node count,
		int	Depth we went down to
	"""

	"""
	populate

	[repeat until found or time is up]
		- getFitness -
		- crossover on best fitnesses -
		get collection of  crossed over organisms
		mutate
	"""

	# create initial population
	population = populate(INITIAL_POPULATION_SIZE, len(operations))

	for x in xrange(1,10):
		
		# get the two fittest organims of out population
		twoFittestOrganism = bestOfPopulation(start, operations, goal, population)
		print 
		print "two best organisms: "
		print map(lambda o: o.getChromosome(), twoFittestOrganism)
		print map(lambda o: o.operate(start, operations), twoFittestOrganism)
		print ".."
		print "... crossing over ..."
		print ".."

		# crossover the two fittest organisms
		crossedOverOrganisms = []
		organisms1, organisms2 = twoFittestOrganism[0].crossover(twoFittestOrganism[1])
		crossedOverOrganisms.append(organisms1)
		crossedOverOrganisms.append(organisms2)
		print "two organisms created by crossover: "
		print map(lambda o: o.getChromosome(), crossedOverOrganisms)
		print "Operation val: " + str(map(lambda o: o.operate(start, operations), crossedOverOrganisms))
		print "Fitness val: " + str(map(lambda o: o.getFitness(start, operations, goal), crossedOverOrganisms))
		print


		# mutate the product of the crossover (2 organisms)
		# population = the collection of mutated organisms
		population = getMutatedPopulation(twoFittestOrganism, INITIAL_POPULATION_SIZE)
		# print "mutated population: " + str(map(lambda o: o.getChromosome(), population))

	# print map(lambda o: o.getChromosome(), populate(10, len(operations)))
	return ([[4, operations[0], 11]], 0.5, 5, 3)


def populate(initSize, numOps):
	population = []
	for i in xrange(initSize):
		population.append(Organism(numOps))
	return population


# Utility function for fitness
def fitnessUtility(lengthOfOrganism):
	# penalize longer organisms
	return lengthOfOrganism * 0.1


# function that returns a new population of the organisms with 
# the best fitness from the given population
def bestOfPopulation(start, operations, goal, population):
	sortedPopulation =  sorted(population,key =lambda o: o.getFitness(start, operations, goal))
	return sortedPopulation[0:2]


# returns a new population of mutated organisms
def getMutatedPopulation(twoFittestOrganism, populationSize):
	mutatedPopulation = []

	# create population of size, populationSize
	for x in xrange(0, populationSize / 2):
		mutatedPopulation.extend(twoFittestOrganism)

	# mutate each organism in population
	for organism in mutatedPopulation:
		organism.mutate(MUTATEPROB)
		# print organism.getChromosome()

	# for x in xrange(0,populationSize):
	# 	if x % 2 == 0:
	# 		newOrganism = twoFittestOrganism[0]
	# 	else:
	# 		newOrganism = twoFittestOrganism[1]

	# 	newOrganism.mutate(MUTATEPROB)
	# 	print newOrganism.getChromosome()
	# 	mutatedPopulation.append(newOrganism)

	return mutatedPopulation


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

	
	# Mutates the organism either by adding, subtracting or modifyinh a gene.
	# Args:
	# 	prob (float): The probability that we will actually mutate. Values of 1 is certain 0 is never.
	def mutate(self, prob=1):
		# Should we mutate?
		if random.random() < prob:
			return 

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
		print cuttingPoint

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
			if index >= len(ops):
				print "EVIL_INDEX " + str(index)
			op = ops[index]
			temp = Functions.operateOn(total, op)
			total = temp
		return total







