import numpy as np

class Organism:
	"""docstring for Organism"""
	gene = []
	def __init__(self):
		self.gene = np.random.randint(5, size=10)

	def printGene(self):
		return self.gene

org = Organism()
print org.printGene()
