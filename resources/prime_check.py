import random


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
