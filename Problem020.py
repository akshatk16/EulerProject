from time import time
from math import factorial
start = time()
n = factorial(100)
sum = 0
for x in str(n):
	sum += int(x)
print(sum)
end = time()
print(end-start)
