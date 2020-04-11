# The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
#
# 1! + 4! + 5! = 1 + 24 + 120 = 145
#
# Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:
#
# 169 → 363601 → 1454 → 169
# 871 → 45361 → 871
# 872 → 45362 → 872
#
# It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
#
# 69 → 363600 → 1454 → 169 → 363601 (→ 1454)
# 78 → 45360 → 871 → 45361 (→ 871)
# 540 → 145 (→ 145)
#
# Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.
#
# How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

from time import time


start = time()

limit = 10**6 + 1
result = 0

factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]


def facsum(num):
	# returns sum of factorials of digits
	sum = 0
	digits = [int(x) for x in str(num)]
	for i in digits:
		sum += factorials[i]
	return sum


for i in range(limit):
	count = 0
	n = i
	last = 0
	while (n != last and n != 169 and n != 363601 and n != 1454 and n != 871 and n != 45361 and n != 872 and n != 45362):
		# given numbers used
		last = n
		n = facsum(n)
		count += 1

	if (count == 57 and (n == 169 or n == 363601 or n == 1454)):
		result += 1

print(result)


end = time()
print(int((end-start)*1000), "ms")
