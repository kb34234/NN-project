import numpy as np

class BAM:
	def __init__(self, inputs, targets):
		self.w = np.zeros((len(inputs[0]), len(targets[0])))
		for i in range(len(inputs)):
			s = np.array(inputs[i])
			t = np.array(targets[i])
			self.w += np.outer(s,t)

	def recall_target(self, inp):
		inp = np.array(inp)
		y_in = np.zeros(3)
		for i in range(3):
			y_in[i] = np.inner(inp, self.w[:,i])
		y = np.zeros(3)
		for i in range(3):
			if y_in[i] > 0:
				y[i] = 1
			else:
				y[i] = -1

		return tuple(y)

	def recall_input(self, tar):
		tar = np.array(tar)
		y_in = np.zeros(100)
		for i in range(3):
			y_in += tar[i] * self.w.transpose()[i]
		y = np.zeros(100)
		for i in range(100):
			if y_in[i] > 0:
				y[i] = 1
			else:
				y[i] = -1

		return tuple(y)