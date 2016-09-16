import numpy as np
import random

NUMOPS = 5

class Organism:
	"""docstring for Organism"""
	#This is an encoding for the solution into an organism
	#each number is an index into the operators we read in.
	chromosome = []
	#The number of operators that we read in, it's used to
	# encode and mutate organisms
	numOps = 0

	def __init__(self, numOps):
		self.chromosome = np.random.randint(numOps, size=10).tolist()
		self.numOps = numOps

	def getGene(self):
		return self.chromosome

	def mutate(self):
		mType = random.randint(1, 3)
		if mType == 1:
			#We are adding a gene as an encoded index
			op = random.randint(0, self.numOps)
			self.chromosome.append(op)
		elif mType == 2:
			#We are removing genes
			i = random.randint(1, len(self.chromosome))
			self.chromosome.pop(i)
		elif mType == 3:
			#We are modigying a gene
			i = random.randint(1, len(self.chromosome))
			self.chromosome[i] = random.randint(1, self.numOps)

org = Organism(NUMOPS)
print org.getGene()
org.mutate()
print org.getGene()
