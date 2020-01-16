# longest recurring decimal length for denominator with integers less than 1000

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


def long_division(denominator):

	# setting numerator as 10, 100, 1000 etc
	numerator = '1'
	for i in range(len(str(denominator))):
		numerator += '0'
	numerator = int(numerator)

	temp = numerator

	q = ''

	for i in range(denominator):
		q += str(numerator // denominator)
		numerator = numerator % denominator

		if numerator < denominator:
			numerator *= 10
			# condition to add decimal point

			if numerator < denominator:
				numerator *= 10
				q += '0'
				# condition to add 0 after decimal

				if numerator < denominator:
					numerator *= 10
					q += '0'
					# condition to add another 0 after decimal

		if numerator == temp:
			return len(q)


record = [[]]
primes = sieve(1000)
for i in primes:
	rec_len = long_division(i)
	if rec_len:
		record.append([rec_len, i])
print(max(record))


end = time()
print(int((end-start)*1000), "ms")
