# Consider the fraction, n/d, where n and d are positive integers.
# If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
#
# If we list the set of reduced proper fractions for d ≤ 8 in ascending order
# of size, we get:
#
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
# 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
#
# It can be seen that there are 21 elements in this set.
#
# How many elements would be contained in the set of reduced proper fractions
# for d ≤ 1,000,000?


from time import time


start = time()

# Using Farey's sequence and totient formula,
# ∣Fn+1​∣=∣Fn​∣ + φ(n+1)
#
# this can be reduced to sum over totients of all numbers from 2 to limit
#
# this can be redued using property of totient that says
# φ(n) = n * {p∣n}∏​(1−1/p​)


limit = 10**6 + 1
sum = 0
phi = [i for i in range(limit)]
# max φ(i) = i-1
# array keeps check if φ(i) is already evaluated

for i in range(2, limit):
	if phi[i] == i:  # check if not evaluated already -> i is prime
		for j in range(i, limit, i):  # evaluating totient for all multiples of i
			phi[j] *= 1 - 1/i  # multiplying by given formula above
	sum += phi[i]  # summing reqd totient values
print(int(sum))

end = time()
print(int((end-start)*1000), "ms")
