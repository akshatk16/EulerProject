# largest Pandigital prime

from time import time
from itertools import permutations
from functools import reduce


start = time()


def check_primality(num):
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


def perms_pandigital(n):
	for i in permutations(range(n, 0, -1)):  # generating permutations
		num = reduce(lambda x, y: 10 * x + y, i)  # converting to number
		if check_primality(num):
			print(num)
			return True


# sum of digits from 1 to n, where n is
# 1=1
# 2=3
# 3=6
# 4=10
# 5=15
# 6=21
# 7=28
# 8=36
# 9=45
#
# all sums except n=1, 4, 7 are divisible by 3
# any permutation of the digits with n other than 1/4/7 would be divisible by 3
# pandigital with length 1 is 1 which is not prime so we dont check for 1 digit


if not perms_pandigital(7):  # check for 7 digits
	perms_pandigital(4)  # check for 4 digits


end = time()
print(int((end-start)*1000), "ms")
