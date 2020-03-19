# Euler's Totient function, φ(n) [sometimes called the phi function],
# is used to determine the number of numbers less than n which are relatively prime to n.
# For example, as 1, 2, 4, 5, 7, and 8, are all less than nine
# and relatively prime to nine, φ(9)=6.
#
# It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.
#
# Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

from time import time


start = time()

N = 100  # do not require more primes


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


def rel_prime_count(num):
	factors = set()
	n = num

	if num in primes:
		# decrease computation time
		return num - 1

	for p in primes:
		# find prime factors
		if p > ((n / 2) + 1):
			break
		while num % p == 0:
			factors.add(p)
			num /= p
	# print(factors)

	res = n
	for i in factors:
		res *= (1 - 1 / i)  # totient formula

	return res


rec = 0, 0
for i in range(2, 1000000):
	t = i / rel_prime_count(i)
	if t > rec[1]:
		rec = i, t
print(rec)

end = time()
print(int((end-start)*1000), "ms")
