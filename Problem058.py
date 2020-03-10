# Starting with 1 and spiralling anticlockwise in the following way,
# a square spiral with side length 7 is formed.
#
# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49
#
# It is interesting to note that the odd squares
# lie along the bottom right diagonal,
# but what is more interesting is that
# 8 out of the 13 numbers lying along both diagonals are prime;
# that is, a ratio of 8/13 ≈ 62%.
#
# If one complete new layer is wrapped around the spiral above,
# a square spiral with side length 9 will be formed.
# If this process is continued,
# what is the side length of the square spiral for which
# the ratio of primes along both diagonals first falls below 10%?


# generating formulae for four diagonals
# b_r = 4 * k ** 2 + 4 * k + 1
# t_r = 4 * k ** 2 - 2 * k + 1
# t_l = 4 * k ** 2 + 0 * k + 1
# b_r = 4 * k ** 2 + 2 * k + 1

from time import time
import random


start = time()


def miller_rabin_primality_test(num):
	if num == 2 or num == 3:
		return True
		
	s = num - 1
	t = 0

	while s % 2 == 0:

		# keep halving s while it is even (and use t
		# to count how many times we halve s)
		s = s // 2
		t += 1

	for trials in range(5):  # try to falsify num's primality 5 times
		a = random.randrange(2, num - 1)
		v = pow(a, s, num)
		if v != 1:  # this test does not apply if v is 1.
			i = 0
			while v != (num - 1):
				if i == t - 1:
					return False
				else:
					i = i + 1
					v = (v ** 2) % num
	return True


k = 1
count, total = 0, 1
while True:

	# generating corners
	b_r = 4 * k ** 2 + 4 * k + 1
	t_r = 4 * k ** 2 - 2 * k + 1
	t_l = 4 * k ** 2 + 0 * k + 1
	b_l = 4 * k ** 2 + 2 * k + 1

	count += miller_rabin_primality_test(b_r)
	count += miller_rabin_primality_test(t_r)
	count += miller_rabin_primality_test(t_l)
	count += miller_rabin_primality_test(b_l)

	# computing ratio
	ratio = count / (total + 4)

	if ratio < 0.1:
		break

	total += 4
	k += 1

print(2 * k + 1)  # computing side length

end = time()
print(int((end-start)*1000), "ms")
