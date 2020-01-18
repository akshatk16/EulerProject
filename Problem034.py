# sum of numbers which can be expressed as
# sum of factorials of its digits
# excluding trivial solutions, i.e. 1, 2

# upper bound is 7*9!=2540160 since
# 8*9! also has 7 digits and can be at max 9999999


from time import time
from math import factorial


start = time()


def chk_factorion(num):
	digits = [int(x) for x in str(num)]
	sum = 0
	for i in digits:
		sum += factorial(i)
	if sum == num:
		print(num)
		return True


factorion = 0

for i in range(10, 2540161):  # 3!=6 and other 1 digit nos do not satisfy
	if chk_factorion(i):
		factorion += i
print("sum =", factorion)


end = time()
print(int((end-start)*1000), "ms")
