import Recallnet
import Matchingnet
import hamming
import time

global encoding
global decoding
def get_sample(path):
	f = open(path, 'r')
	for line in f:
		wavelengths = []
		for w in line.strip().split():
			try:
				wavelengths.append(int(w))
			except:
				return 'error'
		while len(wavelengths) != 10:
			wavelengths.append(0)
		yield wavelengths

def get_reference(path):
	data = []
	f = open(path, 'r')
	for line in f:
		a = line.strip().split()
		code = encoding[a[0]]
		lst = list(map(int, a[1:]))
		while len(lst) < 10:
			lst.append(0)
		data.append((code, tuple(lst)))

	return data

def main():
	global encoding, decoding
	decoding = {(-1,-1,-1): 'H', (-1,-1,1): 'He', (-1,1,-1): 'Li', (-1,1,1): 'O', (1,-1,-1): 'Al', (1,-1,1): 'C', (1,1,-1): 'Zn', (1,1,1): 'N'}
	encoding = {'H': (-1,-1,-1), 'He': (-1,-1,1), 'Li': (-1,1,-1), 'O': (-1,1,1), 'Al': (1,-1,-1), 'C': (1,-1,1), 'Zn': (1,1,-1), 'N': (1,1,1)}
	probabilites = {'H': 0, 'He': 0, 'Li': 0, 'O': 0, 'Al': 0, 'C': 0, 'Zn': 0, 'N': 0}
	data = get_reference('data.txt')
	a = Matchingnet.BAM([to_bipolar(x[1]) for x in data], [x[0] for x in data])
	b = Recallnet.AutoAssociative()

	#Configure hamming net
	lst = []
	for i in decoding:
		lst.append(list(a.recall_input(i)))

	c = hamming.HammingNet(100,8)
	c.store(lst)

	wavelengths = get_sample('sample.txt')

	for lengths in wavelengths:
		lengths = to_bipolar(lengths)
		match = c.recall(lengths)
		element = decoding[a.recall_target(match)]
		print('Element identified:', element)
		dist = hamming_dist(match, lengths)
		prob = (100-dist)/100
		if b.recall(match):
			probabilites[element] = (probabilites[element] + prob)/2 
		else:
			b.store(match)
			probabilites[element] = prob

		time.sleep(10)

	print('Probabities of elements:', probabilites)

def to_bipolar(lst):
	bipolar = []
	for num in lst:
		ls = []
		a = bin(num)
		for n in a[2:]:
			n = int(n)
			if n == 1:
				ls.append(1)
			else:
				ls.append(-1)
		while len(ls) != 10:
			ls.insert(0,-1)
		bipolar = bipolar + ls

	return bipolar


def hamming_dist(a, b):
	hamming = 0
	for i in range(len(a)):
		if a[i] != b[i]:
			hamming += 1

	return hamming

if __name__ == '__main__':
		main()