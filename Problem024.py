# 1000000th Lexicographic permutation

from time import time
from math import factorial


start = time()

N = 1000000

# permutations in the form of (n-1)! * n


def permutation_n(n, digits):
	if len(digits) == 1:  # last digit
		return digits
	q, r = divmod(n, factorial(len(digits)-1))
	# all perms with same digit in same column
	return digits[q] + permutation_n(r, digits[:q] + digits[q+1:])
	# q adds to the required permutation as next digit
	# recursively call the function for unused digits


end = time()
print(permutation_n(N-1, '0123456789'))
print(int((end-start)*1000), "ms")
