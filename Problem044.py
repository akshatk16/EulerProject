# Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2.
# The first ten pentagonal numbers are:

# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

# It can be seen that P4 + P7 = 22 + 70 = 92 = P8.
# However, their difference, 70 − 22 = 48, is not pentagonal.

# Find the pair of pentagonal numbers, Pj and Pk,
# for which their sum and difference are pentagonal and
# D = |Pk − Pj| is minimised;
# what is the value of D?


from time import time


start = time()


def is_pentagonal(num):

	# n = (sqrt(24*num + 1) + 1)/6
	# if n is int, x is pentagonal

	n = (num * 24 + 1) ** 0.5
	if n % 6 == 5:  # using modulus operations
		return True


N = 3000  # upper limit, can be easily scaled
pentagonal_numbers = [0] * N
for i in range(1, N):
	pentagonal_numbers[i] = i * (3*i - 1) // 2

i, flag = 1, 0
while(i < N and flag == 0):
	for j in range(i-1, 0, -1):

		sum = pentagonal_numbers[i] + pentagonal_numbers[j]
		diff = pentagonal_numbers[i] - pentagonal_numbers[j]

		if is_pentagonal(sum):
			if is_pentagonal(diff):
				print(i, j, sum, diff)
				flag = 1

	i += 1


end = time()
print(int((end-start)*1000), "ms")
