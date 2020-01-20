# Number of primes under a given limit whose all rotations are primes as well
# eg: 197, 971, 719 are all primes


from time import time


start = time()

N = 1000000


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
circular_primes = set([2, 3, 5, 7])  # set to avoid repetitions
# single digit primes added since they are always circular primes


def chk_cycle(num):
	for i in range(len(str(num))):
		temp = num % 10
		num = int(str(temp) + str(num // 10))
		# rotated the digits

		if num not in primes:
			return  # not circular prime

	circular_primes.add(num)
	return


for i in range(N):
	flag = 0
	digits = [int(x) for x in str(i)]
	for j in digits:
		if j % 2 == 0 or j % 5 == 0:
			# circular prime cant have digits 0, 2, 4, 5, 6 or 8
			flag = 1
			break
	if flag == 0:
		chk_cycle(i)


print(len(circular_primes))


end = time()
print(int((end-start)*1000), "ms")
