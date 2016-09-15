import numpy as np

# import the actual functions from Functions.py:
import Functions

class Organism:
	"""docstring for Organism"""
	gene = []
	def __init__(self):
		self.gene = np.random.randint(5, size=10)

	def printGene(self):
		return self.gene

	# Returns the product of all operations in the gene
	def operate(self, start):
		total = start

		for index in self.gene:
			# Todo: listOfOperations requires a masterlist of all possible operations.
			operation = listOfOperations[index]
			temp = Functions.operateOn(total, operation)
			total = temp

		return total

	def getFitness(self, desiredGoal):
		goal = desiredGoal
		total = 0
		numOps = 0

		total = self.operate
		difference = diff


			

org = Organism()
print org.printGene()