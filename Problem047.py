# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have
# four distinct prime factors each. What is the first of these numbers?


from time import time


start = time()

N = 100000


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


primes = sieve(N)


def num_prime_factors(num):
	factors = set()  # for unique factors
	n = num ** 0.5
	for i in primes:
		if i > 2*n:
			break
		if num % i == 0:
			factors.add(i)
			num /= i
	return (len(factors))


num = 2 * 3 * 5 * 7  # lower bound

while True:
	if (num_prime_factors(num) == 4):
		num += 1
		if (num_prime_factors(num) == 4):
			num += 1
			if (num_prime_factors(num) == 4):
				num += 1
				if (num_prime_factors(num) == 4):
					print(num-3, 4)
					break
	num += 1


end = time()
print(int((end-start)*1000), "ms")
