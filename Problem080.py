from time import time
from sympy import sqrt


start = time()


max = 100

squares = []
for i in range(int(max ** 0.5) + 1):
	squares.append(i ** 2)


total = 0
for i in range(1, 101):
	if i in squares:
		continue

	num = sqrt(i).evalf(110)
	num = str(num)

	for j in range(101):
		if num[j] == '.':
			continue
		total += int(num[j])

print(total)


end = time()
print(int((end-start)*1000), "ms")
