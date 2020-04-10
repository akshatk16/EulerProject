# Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
# The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.
#
# Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.
#
# Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.


from time import time


start = time()

L = 10**7
lb = 2000
ub = 4000
# lb and ub are around sqrt(L), thus prouct would be around L and reduces search


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
	for i in range(lb, n):  # disregard primes less than lb
		if is_prime[i]:
			primes.append(i)
	return primes


def is_perm(a, b):
	return sorted(str(a)) == sorted(str(b))
	# simple function to return if two numbers are perms


primes = sieve(ub)  # generating primes b/w lb and ub


def perm_totient(L):
	q_min, n_min, i = 2, 0, 0  # set min reqts
	for prime1 in primes:
		i += 1  # counter
		for prime2 in primes[i:]:
			if (prime1 + prime2) % 9 != 1:  # perm condition
				continue
			n = prime1 * prime2  # generating potential result
			if n > L:
				return n_min
			phi = (prime1 - 1) * (prime2 - 1)  # using wiki's definition
			q = n / float(phi)  # reqd equation
			if is_perm(phi, n) and q_min > q:  # reqd q must be min
				q_min, n_min = q, n
	return 0


print(perm_totient(L))

end = time()
print(int((end-start)*1000), "ms")
