# The arithmetic sequence, 1487, 4817, 8147,
# in which each of the terms increases by 3330,
# is unusual in two ways:
# (i) each of the three terms are prime, and
# (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes
# exhibiting this property, but there is one other 4-digit increasing sequence.
#
# What number do you form by concatenating the three terms in this sequence?

from time import time


start = time()


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


def is_perm(a, b):
	p = [0] * 10
	while a:
		p[a % 10] += 1
		a //= 10
	while b:
		p[b % 10] -= 1
		b //= 10

	for i in p:
		if i != 0:
			return False
	return True


primes = sieve(10000)
primes = [x for x in primes if x > 1487]


def main():
	for a in range(1489, 3333):
		if a in primes:
			for b in range(a+1, 6666):
				if is_perm(a, b) and b in primes:
					diff = b - a
					c = b + diff
					if is_perm(c, b) and c in primes:
						print(str(a)+str(b)+str(c))
						return


if __name__ == "__main__":
	main()


end = time()
print(int((end-start)*1000), "ms")
