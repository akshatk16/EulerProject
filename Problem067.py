from time import time


start = time()

# Find the maximum total from top to bottom in triangle.txt, containing a triangle with one-hundred rows.

# converting given text to 2d int list
f = open("p067_triangle.txt")
data = f.read()
triangle = data.strip().split('\n')

for i in range(0, len(triangle)):
	triangle[i] = triangle[i].strip().split(' ')
	triangle[i] = [int(x) for x in triangle[i]]


#recursively find max sum for 2 row triangles and dynamically increase the triangle size
for i, j in [(i, j) for i in range(len(triangle)-2,-1,-1) for j in range(i+1)]:
	triangle[i][j] += max([triangle[i + 1][j], triangle[i + 1][j + 1]])

print(triangle[0][0])


end = time()
print(int((end-start)*1000), "ms")
