# product of a,b for equation n^2 + a*n + b that gives most consecutive primes
# a <  |1000|
# b <= |1000|

from time import time


start = time()

def prime_check(num):
	# skipping all multiples of 2, 3 and decreasing time complexity
	if num < 0:
		return False
	if num % 2 == 0:
		return False
	if num % 3 == 0:
		return False

	for i in range(5, int(num ** 0.5 + 1), 6):
		if num % i == 0:
			return False
		if num % (i + 2) == 0:
			return False
	return True


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


def count_primes(a, b):
	for n in range(0, 1000):
		# given formula
		num = n * n + a * n + b

		if prime_check(num) is False:
			return n


primes = sieve(1000)

max_count, max_prod, count = 0, 0, 0
for a in range(-999, 1000, 2):
	for i in range(len(primes)):
		# by putting 0 in equation, we know that b must be prime
		# by putting 1 in equation, we know that a must be odd

		B = primes[i]

		if i == 0:
			A = a - 1
		else:
			A = a

		count = count_primes(A, B)

		if count is None:
			count = 0

		if max_count < count:
			max_count = count
			max_prod = A * B
			maxA = A
			maxB = B

print("a = {}".format(maxA), "b = {}".format(maxB), "a * b = {}".format(max_prod))
print("Primes generated are {}".format(max_count))


end = time()
print(int((end-start)*1000), "ms")
