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

class Organism:
	"""An Organism represents an encoding of a solution within it's chromosome"""

	#This is an encoding for the solution into an organism
	#each number is an index into the operators we read in.
	chromosome = []
	#The number of operators that we read in, it's used to
	# encode and mutate organisms
	numOps = 0

	def __init__(self, numOps, geneSeq=None):
		self.numOps = numOps
		if geneSeq == None:
			self.chromosome = np.random.randint(5, size=3).tolist()
		else:
			self.chromosome = geneSeq
		
	def getChromosome(self):
		return self.chromosome

	def getLen(self):
		return len(self.chromosome)

	def getFitness(self, base, ops, goal):
		"""
		Defines the organisms fitness given the operations and starting base number.
		Args:
			base (float): The starting number we read.
			ops (OperationStruct[]): An array of operations we read form config file.
			goal (float): The desired goal of base after operations.
		Returns:
			How close the organism is to the desired value once decoded.
		"""
		# Todo: need to penalize for chromosome length
		total = self.operate(base, ops)
		return Functions.diff(total, goal)

	def mutate(self):
		mType = random.randint(1, 3)
		if mType == 1:
			#We are adding a gene as an encoded index
			op = random.randint(0, self.numOps)
			self.chromosome.append(op)
		elif mType == 2:
			#We are removing genes
			i = random.randint(0, len(self.chromosome)-1)
			self.chromosome.pop(i)
		elif mType == 3:
			#We are modigying a gene
			i = random.randint(1, len(self.chromosome))
			self.chromosome[i] = random.randint(1, self.numOps)

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

		newOrganismGene1 = primary[0:cuttingPoint].extend(secondary[cuttingPoint:(len(secondary) - 1)])
		newOrganismGene2 = secondary[0:cuttingPoint].extend(primary[cuttingPoint:(len(primary) - 1)])

		return (Organism(self.numOps, geneSeq=newOrganismGene1), Organism(self.numOps, geneSeq=newOrganismGene2))

	def operate(self, base, ops):
		""" 
		Goes through each encoded operation in the chromosome and applies that to the base.

		Args:
			start (int): The base number form our config file.
			ops (OperationStruct[]): An array of operations we read from config file.
		"""
		total = base

		for index in self.chromosome:
			op = ops[index]
			temp = Functions.operateOn(total, op)
			total = temp
		return total

def populate(initSize, numOps):
	population = []
	for i in xrange(initSize):
		population.append(Organism(numOps))
	return population

def geneticSearch(base, operations, goal, max_exec):
	"""
	Returns:
		[int, OperationStruct, int][] The solution path we took to solve,
		int	Execution time,
		int	Expanded node count,
		int	Depth we went down to
	"""
	return ([[4, operations[0], 11]], 0.5, 5, 3)

	# print map(lambda o: o.getChromosome(), populate(10, len(operations)))

# org = Organism(NUMOPS)
# print org.getChromosome()
# org.mutate()
# print org.getChromosome()

# org = Organism(numOps=len(operations))
# org2 = Organism(numOps=len(operations))
# print org.getChromosome()
# print org2.getChromosome()

# new1, new2 = org.crossover(org2)
# print new1.getChromosome()
# print new2.getChromosome()