# By counting carefully it can be seen that a rectangular grid measuring 3 by 2
# contains eighteen rectangles.
# Although there exists no rectangular grid that contains exactly two million
# rectangles, find the area of the grid with the nearest solution.

from time import time


start = time()

lim = 2000000  # required target


def rectCount(n, m):
	return (m * n * (n + 1) * (m + 1)) // 4  # generating total no. of rects


min = float('Inf')  # error term
area = 0  # area of reqd rect
rec = 0  # closest to target


x = 100  # starting postitions
y = 1

while x >= y:
	count = rectCount(x, y)
	if abs(count - lim) < min:  # check error
		min = abs(count - lim)
		area = x * y
		rec = count
	if count > lim:
		x -= 1
	else:
		y += 1

print("Closest number of rectangles than can be formed to", lim, "are", rec)
print("Required area is", area)
end = time()
print(int((end-start)*1000), "ms")
