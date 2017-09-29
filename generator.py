import random

frags = ["A", "C", "T", "G"]

def generate(num):
	dna_seq = []
	for i in range(num):
		dna_seq.append(random.choice(frags))
	return dna_seq
	