# It was proposed by Christian Goldbach that
# every odd composite number can be written as
# the sum of a prime and twice a square.
#
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that
# cannot be written as the sum of a prime and twice a square?


from time import time


start = time()


def sieve(n):
	# Sieve of Erastosthenes to generate primes upto n

	is_prime = [True]*n
	is_prime[0] = False
	is_prime[1] = False
	for odd_comp in range(2, int(n**0.5+1)):
		index = odd_comp * 2
		while index < n:
			is_prime[index] = False
			index = index+odd_comp
	primes = []
	for odd_comp in range(n):
		if is_prime[odd_comp]:
			primes.append(odd_comp)
	return primes


primes = sieve(10000)

odd_comp = 3  # odd composite number to be checked for

found = True
while (found):
	if odd_comp not in primes:  # primes not considered
		found = False
		for prime in primes:  # first addend
			if prime < odd_comp:
				if (((odd_comp-prime)/2)**0.5) == int(((odd_comp-prime)/2)**0.5):
					# number twice squared must be integer
					found = True
					break
		if (not found):  # no integers found for second addend
			print(odd_comp)
	odd_comp += 2


end = time()
print(int((end-start)*1000), "ms")
