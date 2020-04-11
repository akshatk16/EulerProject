# Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
#
# If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
#
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
#
# It can be seen that there are 3 fractions between 1/3 and 1/2.
#
# How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?

from time import time


start = time()

result = 0

n = 12000
a = 1
b = 3

# finding last number in sequence
for d in range(n + 1, 1, -1):
	c = (1 + a*d) / b
	if int(c) == c:
		break

c = int(c)

# using Farey sequences, following formulae give next fraction
while not(c == 1 and d == 2):
	factor = int((n + b) / d)
	e = factor * c - a
	f = factor * d - b
	a, b, c, d = c, d, e, f
	result += 1

print(result)

end = time()
print(int((end-start)*1000), "ms")
