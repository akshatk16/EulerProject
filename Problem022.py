# sum of namescore defined as position in sorted order and sum of letter equivalents in given list of names

from time import time


letters={
				"A":1,
				"B":2,
				"C":3,
				"D":4,
				"E":5,
				"F":6,
				"G":7,
				"H":8,
				"I":9,
				"J":10,
				"K":11,
				"L":12,
				"M":13,
				"N":14,
				"O":15,
				"P":16,
				"Q":17,
				"R":18,
				"S":19,
				"T":20,
				"U":21,
				"V":22,
				"W":23,
				"X":24,
				"Y":25,
				"Z":26
			   }


start = time()

file = open("p022_names.txt", "r")
names = sorted(file.read().replace('"', '').split(','), key=str)
# file given with commas as seperators and contain "" around names

total_sum = 0
for i, j in enumerate(names):
	sum = 0
	for ele in j:
		sum += letters[ele]
	total_sum += sum * (i+1)

file.close()

print(total_sum)

end = time()
print(int((end-start)*1000), "ms")
