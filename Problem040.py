# product of required digits in champernowne's constant

from time import time


start = time()

d = [0]  # accouting for difference in index and digit
i = 1
# making list with the digits
while len(d) < 1000001:
	temp = [int(x) for x in str(i)]
	d.extend(temp)
	i += 1

res = d[1] * d[10] * d[100] * d[1000] * d[10000] * d[100000] * d[1000000]
print(res)


end = time()
print(int((end-start)*1000), "ms")
