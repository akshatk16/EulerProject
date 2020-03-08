# By replacing the 1st digit of the 2-digit number *3,
# it turns out that six of the nine possible values:
# 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit,
# this 5-digit number is the first example having seven primes
# among the ten generated numbers, yielding the family:
# 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
# Consequently 56003, being the first member of this family,
# is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number
# (not necessarily adjacent digits)
# with the same digit, is part of an eight prime value family.


from time import time
from collections import Counter


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


primes = sieve(1000000)
primes = [x for x in primes if len(str(x)) - len(set(str(x))) >= 3]
# only primes with 3 or more replacable digits


def get_family(s):
	dig = str(s)
	res = []
	for duplicate in (Counter(dig) - Counter(set(dig))):
		a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
		temp = [int(dig.replace(duplicate, x)) for x in a]
		# returns all possible families for given number
		res.append(temp)
		return res


checked = []


def prime_chk(l):
	# checks if number in the family is prime or not
	for i in l:
		checked.append(i)
		if i not in primes:
			l.remove(i)
	return l


flag = True
i = 0
while flag:
	if primes[i] not in checked:
		iters = get_family(primes[i])
		for j in iters:
			if len(prime_chk(j)) == 8:
				print(j[0])
				flag = False
				break
	i += 1

end = time()
print(int((end-start)*1000), "ms")
