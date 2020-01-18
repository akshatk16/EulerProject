# the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# by analysis, it can be seen that for a 7 digit number,
# the maximum sum of digits to fifth power is
# 7 * (9**5) = 413343
# which is a 6 digit number.
# Thus, maximum 6 digits can be achieved since,
# 6 * (9**5) = 354294
# This is the upper limit for the analysis


from time import time


start = time()

def check_sum(num):
	sum, chk = 0, num
	while num > 0:
		temp = num % 10
		sum += temp ** 5
		num //= 10
	if sum == chk:
		return True
	return False


total_sum = 0
for i in range(2, 354295):
	if check_sum(i):
		total_sum += i
print(total_sum)


end = time()
print(int((end-start)*1000), "ms")
