# Sum of diagonals in n*n square spiral

# example with 5*5 square
# 21...22...23...24....25
# 20....7....8....9....10
# 19....6....1....2....11
# 18....5....4....3....12
# 17...16...15...14....13
# sum = 101


# solution
# skipping 1, 4 digaonals can be found, namely:
# diag_1 = {3, 13, 31, 57, ...}
# diag_2 = {5, 17, 37, 65, ...}
# diag_3 = {7, 21, 43, 73, ...}
# diag_4 = {9, 25, 49, 81, ...}

# for each diagonal, a generating sequence may be derived as follows:
# diag_1 = 4 * (n ** 2) - 2 * (n) + 1
# diag_2 = 4 * (n ** 2) + 0 * (n) + 1
# diag_3 = 4 * (n ** 2) + 2 * (n) + 1
# diag_4 = 4 * (n ** 2) + 4 * (n) + 1

# total_sum = (1 + for i in range(k):
# 			 			sum(diag_1(i)) +
# 			 			sum(diag_2(i)) +
# 			 			sum(diag_3(i)) +
# 			 			sum(diag_4(i))
# 			  )
# total_sum = 1 + for i in range k:
# 					16 * (i ** 2) + 4 * (i) + 4

# sum of squares = k(k+1)(2k+1)/6
# sum of natural numbers = k(k+1)/2
# sum of 1s = k

# total_sum = 1 +
# 			  16 * k(k+1)(2k+1)/6 +
# 			  4  * k(k+1)/2 +
# 			  4  * k

# total_sum = 1 +
# 			  16/3 k^3 +
# 			  10   k^2 +
# 			  26/3 k

# for a spiral with 2 sqaures(k) excluding center, length of outermost square is 5
# for n side square, no. of sqaures is n-1/2

from time import time


start = time()

length = 1001


def poly(k):
	res = (16/3) * (k ** 3) + (10) * (k ** 2) + (26/3) * (k) + 1
	# compute the result using derived polynomial
	return round(res)


print(poly((length - 1)//2))  # k = (n-1)//2


end = time()
print(int((end-start)*1000), "ms")
