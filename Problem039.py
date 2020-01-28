# perimeter of a right triangle that can be formed using integer lengths


# a + b + c = p
# a + b + sqrt(a^2 + b^2) = p
# for b = 0
# 2a = p
# a <= p/2
# without loss of generality, b <= p/2
# a, b < p/2 because all lengths must be > 0


from time import time


start = time()

count = [0] * 1001  # array using index to hold number of possible ways

for a in range(500):
	for b in range(500):
		c = (a ** 2 + b ** 2) ** (0.5)  # pythagoras theorem
		if (c % 1 == 0) and (a + b + c) <= 1000:
			count[a + b + int(c)] += 1
			# incrementing the no. of ways for a given perimeter

max_ways = max([(val, index) for index, val in enumerate(count)])
print(max_ways[1], "can be written in", max_ways[0], "ways")
# priting perimeter with max no. of ways


end = time()
print(int((end-start)*1000), "ms")
