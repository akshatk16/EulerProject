# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
#
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

from time import time
import random


start = time()

# use sieve to generate first 10000 primes
# use miller rabin test to test for higher primes


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


def miller_rabin_primality_test(n):
	if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
		return [False, False, True, True, False, True][n]
	elif n % 2 == 0:  # should be faster than n % 2
		return False
	else:
		s, d = 0, n - 1
		while d % 2 == 0:
			s, d = s + 1, d >> 1
			# A for loop with a random sample of numbers
		for a in random.sample(range(2, n-2), 3):  # falsify 3 times
			x = pow(a, d, n)
			if x != 1 and x + 1 != n:
				for r in range(1, s):
					x = pow(x, 2, n)
					if x == 1:
						return False  # composite for sure
					elif x == n - 1:
						a = 0  # so we know loop didn't continue to end
						break  # could be strong liar, try another a
				if a:
					return False  # composite if we reached end of this loop
		return True  # probably prime if reached end of outer loop


def check_perms_primes(a, b):
	# check if both orders of concatenations are prime
	if miller_rabin_primality_test(int(str(a)+str(b))) and miller_rabin_primality_test(int(str(b)+str(a))):
		return True
	return False


primes = sieve(10000)


def main():
	for a in primes:
		for b in primes:
			if b < a:
				continue
			if check_perms_primes(a, b):
				for c in primes:
					if c < b:
						continue
					if check_perms_primes(a, c) and check_perms_primes(b, c):
						for d in primes:
							if d < c:
								continue
							if check_perms_primes(a, d) and check_perms_primes(b, d) and check_perms_primes(c, d):
								for e in primes:
									if e < d:
										continue
									if check_perms_primes(a, e) and check_perms_primes(b, e) and check_perms_primes(c, e) and check_perms_primes(d, e):
										print(a+b+c+d+e)
										return


if __name__ == "__main__":
	main()


end = time()
print(int((end-start)*1000), "ms")
