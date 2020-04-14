# It is possible to write ten as the sum of primes in exactly five different ways:

# 7 + 3
# 5 + 5
# 5 + 3 + 2
# 3 + 3 + 2 + 2
# 2 + 2 + 2 + 2 + 2

# What is the first value which can be written as the sum of primes in over five thousand different ways?


from time import time


start = time()

req = 5000  # target num of partitions


def sieve(n):
	# Sieve of Erastosthenes to generate primes upto n

	is_prime = [True]*n
	is_prime[0] = False
	is_prime[1] = False
	for i in range(2, int(n**0.5+1)):
		index = i * 2
		while index < n:
			is_prime[index] = False
			index = index+i
	primes = []
	for i in range(n):
		if is_prime[i]:
			primes.append(i)
	return primes


primes = sieve(1000)


def prime_partitions(req):
	num = 2  # variable to check potential solution
	while True:
		partitions = [1] + [0] * num  # array to hold num of partitions

		for i in range(len(primes)):
			for j in range(primes[i], num + 1):
				partitions[j] += partitions[j - primes[i]]

		if partitions[num] > req:
			break
		num += 1

	return partitions


arr = prime_partitions(req)
print(len(arr) - 1, "is the first number to have over", req, "partitions")


end = time()
print(int((end-start)*1000), "ms")
