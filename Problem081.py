# Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt
# a 31K text file containing an 80 by 80 matrix.


from time import time


start = time()

f = open("p081_matrix.txt")
data = f.read()
matrix = data.strip().split('\n')

for i in range(0, len(matrix)):
	matrix[i] = matrix[i].strip().split(',')
	matrix[i] = [int(x) for x in matrix[i]]

l = len(matrix)
for i in range(l-2, -1, -1):  # sum from every vertex till the last
	matrix[l - 1][i] += matrix[l - 1][i + 1]
	matrix[i][l - 1] += matrix[i + 1][l - 1]

for i in range(l - 2, -1, -1):  # minimum solution
	for j in range(l - 2, -1, -1):
		matrix[i][j] += min(matrix[i + 1][j], matrix[i][j + 1])


print(matrix[0][0])

end = time()
print(int((end-start)*1000), "ms")
