# Index of first 1000 digit fibonaci number where F_1 = F_2 = 1

from time import time


start = time()

curr, prev, count = 1, 1, 2
nextF = 0
while len(str(nextF)) < 1000:
	nextF = curr + prev
	prev = curr
	curr = nextF
	count += 1
print(nextF, count)

end = time()
print(int((end-start)*1000), "ms")
