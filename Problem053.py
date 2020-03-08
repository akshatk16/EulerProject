# There are exactly ten ways of selecting three from five, 12345:
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

# In combinatorics, we use the notation, (5C3)=10

# In general, (nCr)=n!r!(n−r)!
# where r≤n, n!=n×(n−1)×...×3×2×1, and 0!=1

# It is not until n=23
# that a value exceeds one-million: (2310)=1144066

# How many, not necessarily distinct, values of (nCr)
# for 1≤n≤100, are greater than one-million?


from time import time


start = time()

N = 100
pascal = [0] * (N + 1)
pascal[N] = 1


def gen_pascal():
	temp = pascal  # current row calculated using previous row
	for i in range(1, N+1):
		pascal[i-1] = temp[i-1]+temp[i]


count = 0
for i in range(N):
	gen_pascal()
	for p in pascal:
		if p > 1000000:  # check condition
			count += 1
print(count)

end = time()
print(int((end-start)*1000), "ms")
