import numpy as np

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
			temp = operateOn(total, operation)
			total = temp

		return total
			

org = Organism()
print org.printGene()