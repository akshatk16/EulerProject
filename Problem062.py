# Find the smallest cube for which exactly five permutations of its digits are cube.

from time import time


start = time()

cubes = []  # stores lowest permutations of all cubes generated
i = 0

while True:
	num = str(i ** 3)
	num = sorted(list(num))  # lowest permutation of two numbers that are permutations of each other would be same
	cubes.append(num)
	if cubes.count(num) == 5:  # check condition
		rec = cubes.index(num)
		break
	i += 1
print(rec ** 3)

end = time()
print(int((end-start)*1000), "ms")
