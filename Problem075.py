# It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.
#
# 12 cm: (3,4,5)
# 4 cm: (6,8,10)
# 30 cm: (5,12,13)
# 36 cm: (9,12,15)
# 40 cm: (8,15,17)
# 48 cm: (12,16,20)
#
# In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.
#
# 120 cm: (30,40,50), (20,48,52), (24,45,51)
# Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?
# Note: This problem has been changed recently, please check that you are using the right parameters.


from time import time


start = time()


def gcd(a, b):
	if b == 0:
		return abs(a)
	return gcd(b, (a % b))


L = 1500000
sols = [0] * (L + 1)  # array to hold number of ways each integer can be constructed
res = 0  # required result
lim = int((L / 2) ** 0.5)  # max m and n values


for m in range(2, lim):
	for n in range(1, m):

		if (n + m) % 2 == 0:  # multiples skipped
			continue
		elif gcd(n, m) != 1:
			continue

		# generating triples
		a = m ** 2 + n ** 2
		b = m ** 2 - n ** 2
		c = 2 * m * n

		# total perimeter
		p = a + b + c

		step = p
		while p <= L:
			sols[p] += 1
			if sols[p] == 1:
				res += 1  # increasing count for every number that has 1 way
			if sols[p] == 2:
				res -= 1  # removing extra solutions that were added previously
			p += step  # a, b, c triples -> ka, kb, kc triples


print(res)


end = time()
print(int((end-start)*1000), "ms")
