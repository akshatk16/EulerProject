# largest 1 to 9 pandigital number
# that can be made using multiplying a fixed number by (1,2, ...,, n)
# where n > 1


from time import time


start = time()


def check_pandigital(num):
	digits = set([int(x) for x in num])

	if 0 in digits:
		return False  # 0 can not be included

	if len(digits) == 9:  # only left possible digits are 1-9
		# print(num, 1)
		return True


def gen_products(n):
	prod = ''
	i = 1
	while len(prod) < 9:  # reqd for 1 to 9 pandigital
		prod += str(n * i)
		i += 1
	if len(prod) == 9:
		if check_pandigital(prod):
			return prod
		else:
			return 0
	else:
		return 0


# number cant be 5 digits long since n > 1
for i in range(9876, 1, -1):
	# must have different digits since num*1 cant have repeating digits
	if prod := gen_products(i):  # python3.8 feature for assignment
	# largest number will be the first encountered since num*1 must return largest starting digits
		break
print(prod)

end = time()
print(int((end-start)*1000), "ms")
