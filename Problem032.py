# sum of all products whose
# multiplicand/multiplier/product identity can be written as
# a 1 through 9 pandigital

# only possible combinations can be:
	#	  a   *     b    =   prod
	# 1 digit * 4 digits = 4 digits
		# b starts from 1234, since it is the smallest 4 digit number without repeating digits
	# 2 digit * 3 digits = 4 digits
		# b starts from 123, since it is the smallest  digit number without repeating digits
	# if product exceeds 4 digits, its unusable,
	# thus optimisation can be made for b to range upto 10000//a





from time import time


start = time()


def check_pandigital(a, b, prod):
	temp = str(a)+str(b)+str(prod)
	# string with all required digits

	digits = set([int(x) for x in temp])
	# set avoids repetition

	if 0 in digits:
		return False  # 0 can not be included

	if len(digits) == 9:  # only left possible digits are 1-9 and require no further checking
		print(a, b, prod)
		return True


prod_sum = set()  # to avoid repetitions
for a in range(2, 99):  # 1 never works
	if a < 10:
		b_low = 1234  # from above explanation
	else:
		b_low = 123  # from above explanation

	for b in range(b_low, 10000//a):  # from above explanation
		prod = a * b
		if check_pandigital(a, b, prod):
			prod_sum.add(prod)
print(sum(prod_sum))


end = time()
print(int((end-start)*1000), "ms")
