# sum of all two sided truncatable prime numbers

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


# binary search reduced execution time from 84s to 1s
def binarySearch(arr, beg, end, x):

	while beg <= end:
		mid = beg + (end - beg)//2

		if arr[mid] == x:  # found
			return True

		elif arr[mid] < x:
			beg = mid + 1

		else:
			end = mid - 1
	return False  # not found


def is_right_truncatable(num):
	while num > 10:
		num = int(str(num)[:-1])  # removing last digit
		if not binarySearch(primes, 0, len(primes), num):
			return False
	return True


def is_left_truncatable(num):
	while num > 10:
		num = int(str(num)[1:])  # removing first digt
		if not binarySearch(primes, 0, len(primes), num):
			return False
	return True


# driver code
sum, count = 0, 0
for i in primes[4:]:  # 2, 3, 5, 7 not considered
	if count < 11:  # given total number of two-sided truncatable primes
		if is_left_truncatable(i):
			if is_right_truncatable(i):
				count += 1
				print(i)
				sum += i
print("sum =", sum)


end = time()
print(int((end-start)*1000), "ms")
