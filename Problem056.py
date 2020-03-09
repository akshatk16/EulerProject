# A googol (10^100) is a massive number:
# one followed by one-hundred zeros;
# 100^100 is almost unimaginably large:
# one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form, ab, where a, b < 100,
# what is the maximum digital sum?

from time import time


start = time()


def dig_sum(num):
	res = [int(dig) for dig in str(num)]  # convert to list
	res = sum(res)  # sum digits
	return res


record = 0
for a in range(100):
	for b in range(100):
		if (res := dig_sum(a**b)) > record:  # check condition
			print(a, b, res)
			record = res
print(record)


end = time()
print(int((end-start)*1000), "ms")
