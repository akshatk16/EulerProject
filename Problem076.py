# It is possible to write five as a sum in exactly six different ways:
#
# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1
#
# How many different ways can one hundred be written as a sum of at least two positive integers?


from time import time


start = time()

req = 100


def pentagonal_number(k):
<<<<<<< HEAD
	num = k * (3 * k - 1) / 2  # euler's pentagonal formula
=======
	num = k * (3 * k - 1) / 2
>>>>>>> ab0ac1956b59d042d8428138d340cd7685b52c1c
	return int(num)


def num_of_partitions(num):
<<<<<<< HEAD
	partitions = [1]  # base case
	for n in range(1, num + 1):  # computing recursively till req num
		partitions.append(0)
		for k in range(1, n + 1):  # recurrence relation
			j = 1
			if k % 2 == 0:  # even k turns sign negative
=======
	partitions = [1]
	for n in range(1, num + 1):
		partitions.append(0)
		for k in range(1, n + 1):
			j = 1
			if k % 2 == 0:
>>>>>>> ab0ac1956b59d042d8428138d340cd7685b52c1c
				j = -1
			for t in [pentagonal_number(k), pentagonal_number(-k)]:
				if (n - t) >= 0:
					partitions[n] = partitions[n] + j * partitions[n - t]
	return partitions


arr = num_of_partitions(req)
print(arr)
print(req, "has", arr[req] - 1, "partitions with at least 2 integers")


end = time()
print(int((end-start)*1000), "ms")
