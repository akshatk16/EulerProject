# product of non trivial examples of fractions less than 1 which can be reduced
# by cancelling the common terms in numerator and denominator
# and give correct answer as in normal reduction

# 49/98 == 4/8  (cancelling 9) valid solution
# 30/50 == 3/5  (cancelling 0) valid solution but trivials

from time import time


start = time()


def gcd(a, b):
	while(b):
		a, b = b, a % b
		# euclid's lemma to find gcd
	return a


def funny_fraction(a, b):
	num = [int(x) for x in str(a)]
	den = [int(x) for x in str(b)]

	# print(num, den)

	for i in num:
		if i in den:  # checking for duplicates
			num.remove(i)
			den.remove(i)
	if den[0] == 0 or len(den) == 2:  # handling division by 0 and no cancellation
		return False
	if a/b == num[0]/den[0]:  # checking required condition
		print(a, "/", b)
		return True


prod_num, prod_den = 1, 1
for den in range(11, 99):  # 2 digit denominator
	for num in range(11, den):  # 2 digit numerator and fraction < 1
		if num % 10 != 0 and den % 10 != 0 and num % 11 != 0 and den % 11 != 0:
			# non trivial cases only
			if funny_fraction(num, den):
				prod_num *= num
				prod_den *= den
print(prod_den//gcd(prod_num, prod_den))  # reduction to simplest form

end = time()
print(int((end-start)*1000), "ms")
