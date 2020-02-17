# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

from time import time


start = time()


mod = 10**10  # for last ten digits
sum = 0

# (a+b)%n = (a%n + b%n)%n
for i in range(1, 1000):
	res = (i**i) % mod
	sum += res
	sum = sum % mod

print(sum)


end = time()
print(int((end-start)*1000), "ms")
