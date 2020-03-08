# Find the smallest positive integer, x, such that
# 2x, 3x, 4x, 5x, and 6x, contain the same digits.


from time import time


start = time()


i = 1
while True:
	if set(str(i)) == set(str(6 * i)):
		if set(str(i)) == set(str(5 * i)):
			if set(str(i)) == set(str(4 * i)):
				if set(str(i)) == set(str(3 * i)):
					if set(str(i)) == set(str(2 * i)):
						print(i)
						break
	i += 1


end = time()
print(int((end-start)*1000), "ms")
