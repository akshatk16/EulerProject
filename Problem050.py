# Which prime, below one-million, can be written as
# the sum of the most consecutive primes?

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


N = 1000000

primes = sieve(N)

sum = 0
for i in primes:
	if sum < N:
		sum += i  # summing consecutive primes
	if sum > N:
		sum -= i  # the sum must be less than a million


record = False
i = 0
while(not record):
	if sum in primes:
		record = True  # required solution
		break
	sum -= primes[i]  # next largest prime
	i += 1

print(sum)


end = time()
print(int((end-start)*1000), "ms")
