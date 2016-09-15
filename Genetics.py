import numpy as np
from random import randint

# import the actual functions from Functions.py:
import Functions

class Organism:
	"""docstring for Organism"""
	gene = []
	def __init__(self, geneSeq=None):
		if geneSeq == None:
			self.gene = np.random.randint(5, size=10).tolist()
		else:
			self.gene = geneSeq

	def printGene(self):
		return self.gene

	def length(self):
		return len(self.gene)

	def getGene(self):
		return self.gene

	def crossover(self, otherOrganism):
		primary = None
		secondary = None
		if self.length() < otherOrganism.length():
			primary = self.getGene()
			secondary = otherOrganism.getGene()
		else:
			primary = otherOrganism.getGene()
			secondary = self.getGene()

		cuttingPoint = randint(0, len(primary) - 1)

		newOrganismGene1 = primary[0:cuttingPoint].extend(secondary[cuttingPoint:(len(secondary) - 1)])
		newOrganismGene2 = secondary[0:cuttingPoint].extend(primary[cuttingPoint:(len(primary) - 1)])

		return (Organism(newOrganismGene1), Organism(newOrganismGene2))

	def operate(self, start):
		total = start

		for index in self.gene:
			# Todo: listOfOperations requires a masterlist of all possible operations.
			operation = listOfOperations[index]
			temp = Functions.operateOn(total, operation)
			total = temp

		return total

org = Organism()
org2 = Organism()
print org.printGene()
print org2.printGene()

new1, new2 = org.crossover(org2)
print new1.printGene()
print new2.printGene()