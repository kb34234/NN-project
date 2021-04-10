import numpy as np

class HammingNet:
	def __init__(self, n, m):
		self.w = np.zeros((n, m))
		self.b = np.zeros(m)
		self.n = n
		self.m = m

	def store(self, exemplar):
		exemplar = np.array(exemplar)
		y_in = np.zeros(self.m)
		for i in range(self.n):
			for j in range(self.m):
				self.w[i,j] = exemplar[j][i]

		for j in range(self.m):
			self.b[j] = self.n/2


	def recall(self, inputs):
		y = np.zeros(self.m)
		y_in = np.zeros(self.m)
		inputs = np.array(inputs)
		for j in range(self.m):
			y_in[j] = self.b[j]
			for i in range(self.n):
				y_in[j] += inputs[i] * self.w[i,j]
			y[j] = y_in[j]

		y = list(y)
		maximum = max(y)
		index = y.index(maximum)
		return list(self.w[:,index])