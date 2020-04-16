# Let p(n) represent the number of different ways in which n coins can be separated into piles.
# For example, five coins can separated into piles in exactly seven different ways, so p(5)=7.
# Find the least value of n for which p(n) is divisible by one million.


from time import time


start = time()

div = 10**6  # target num of partitions


def pentagonal_number(k):
	num = k * (3 * k - 1) // 2  # euler's pentagonal formula
	return num


def num_of_partitions():
	sign = [1, 1, -1, -1]  # according to sign of term in generating function
	partitions = [1]  # for 0 coins
	n = 1  # counter
	while True:
		i, k = 0, 1
		partitions.append(0)

		while k <= n:
			j = sign[i % 4]  # reqd sign for current term
			partitions[n] += j * partitions[n - k]  # updating partitions
			partitions[n] %= div  # storing as mod div
			i += 1  # incrementing i

			t = -(i // 2 + 1)  # generate next k
			if i % 2 == 0:
				t = i // 2 + 1  # for even, sign flips

			k = pentagonal_number(t)  # generate using euler's penta formula

		if partitions[n] == 0:  # checck condition
			break
		n += 1  # increment n
	return partitions


arr = num_of_partitions()
# print(arr)
print(len(arr) - 1, "is the first number to have partition divisible by", div)


end = time()
print(int((end-start)*1000), "ms")
