# Sum of Amicable Numbers where, d(a) = b and d(b) = a, where a ≠ b
from time import time

start = time()

sumF = []
cache = [0] * 10000


def sum_pair(num, chk):
	sum = 0
	if cache[num] != 0:
		for i in range(1, num):
			if num % i == 0:
				sum += i
			if sum > 10000:
				return
		cache[num] = sum
	else:
		sum = cache[num]
	if sum == chk:
		sumF.append(num)
		sumF.append(chk)


def sum_divisors(num):
	sum = 0
	if cache[num] == 0:
		for i in range(1, num):
			if num % i == 0:
				sum += i
			if sum > 10000:
				return
		cache[num] = sum
	else:
		sum = cache[num]
	if sum != num:
		sum_pair(sum, num)
	return


for i in range(0, 10000, 2):
	sum_divisors(i)
print(sum(sumF))

end = time()

print(int((end - start) * 1000), "ms")
