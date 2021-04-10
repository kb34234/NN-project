import numpy as np

class AutoAssociative:
	def __init__(self):
		self.w = np.zeros((100,100))

	def store(self,inp):
		inp = np.array(inp)
		delta_w = np.outer(inp.transpose(),inp)
		self.w = self.w + delta_w


	def recall(self,inp):
		y = np.zeros(100)
		inp = np.array(inp)
		for j in range(3):
			y_in  = np.dot(inp, self.w)
			for k in range(100):
				if y_in[k] > 0:
					y[k] = 1
				else:
					y[k] = -1

			inp = y

		return list(map(int, list(y)))

	def clear(self):
		self.w = np.zeros((100,100))
