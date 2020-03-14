# How many n-digit positive integers exist which are also an nth power?
from time import time


start = time()

count = 0

# the upper bound for the radix must be 9 since:
# 10^1 = 10
# 10^2 = 100
# 10^3 = 1000
# thus, any exponent for a base greater than 9 would return at least n+1 digits
for i in range(1, 10):
	j = 1
	while True:
		t = i ** j
		if len(str(t)) == j:  # check condition
			count += 1
			# print(i, j, t)
		else:  # the length exceeds the exponent once, will never be equal again
			break
		j += 1

print(count)

end = time()
print(int((end-start)*1000), "ms")
