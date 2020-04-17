# How many numbers below fifty million can be expressed as the sum of
# a prime square, prime cube, and prime fourth power?


from time import time


start = time()
lim = 50 * 10 ** 6             # required upper limit
lim_2 = int(lim ** 0.5) + 1    # square root
lim_3 = int(lim ** (1/3)) + 1  # cube root
lim_4 = int(lim ** 0.25) + 1   # fourth root


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


primes = sieve(lim_2)


squares, cubes, quads = [], [], []  # lists to store powers o avoid redundant calculations
for i in primes:
	if i < lim_2:
		squares.append(i ** 2)
	if i < lim_3:
		cubes.append(i ** 3)
	if i < lim_4:
		quads.append(i ** 4)


checked = set()  # records all possible numbers that satisfy the condition

for i in squares:
	for j in cubes:
		for k in quads:
			t = i + j + k  		# generate a number satisfying condition
			if t < lim:  		# check for upper limit
				checked.add(t)  # add to set to avoid duplicates and double counting


print(len(checked), "numbers less than", lim, "can be expressed as a sum of a prime square, a prime cube and a prime fourth power")


end = time()
print(int((end-start)*1000), "ms")
