import numpy as np
import random

# import the actual functions from Functions.py:
import Functions

NUMOPS = 5

class Organism:
	"""docstring for Organism"""
	#This is an encoding for the solution into an organism
	#each number is an index into the operators we read in.
	chromosome = []
	#The number of operators that we read in, it's used to
	# encode and mutate organisms
	numOps = 0

	def __init__(self, numOps=0, geneSeq=None):
		self.numOps = numOps
		if geneSeq == None:
			self.chromosome = np.random.randint(5, size=10).tolist()
		else:
			self.chromosome = geneSeq
		
	def getChromosome(self):
		return self.chromosome

	def getLen(self):
		return len(self.chromosome)

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

		return (Organism(geneSeq=newOrganismGene1), Organism(geneSeq=newOrganismGene2))

	def operate(self, start):
		total = start

		for index in self.gene:
			# Todo: listOfOperations requires a masterlist of all possible operations.
			operation = listOfOperations[index]
			temp = Functions.operateOn(total, operation)
			total = temp

		return total



org = Organism(NUMOPS)
print org.getChromosome()
org.mutate()
print org.getChromosome()

org = Organism(numOps=NUMOPS)
org2 = Organism(numOps=NUMOPS)
print org.getChromosome()
print org2.getChromosome()

new1, new2 = org.crossover(org2)
print new1.getChromosome()
print new2.getChromosome()
