# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
# Triangle 	  	Tn=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
# Pentagonal  	Pn=n(3n−1)/2 	  	1, 5, 12, 22, 35, ...
# Hexagonal   	Hn=n(2n−1) 	 	 	1, 6, 15, 28, 45, ...

# It can be verified that T285 = P165 = H143 = 40755.

# Find the next triangle number that is also pentagonal and hexagonal.


from time import time


start = time()

# hexagonal numbers can be listed using triangular numbers and are thus
# a subset of triangular numbers
# triangular numbers with even indices are hexagonal numbers
# (index starting with 1)
# EVERY HEXAGONAL NUMBER IS TRIANGULAR


def is_pent(num):

	# n = (sqrt(24*num + 1) + 1)/6
	# if n is int, x is pentagonal

	n = (num * 24 + 1) ** 0.5
	if n % 6 == 5:  # using modulus operations
		return True


i = 144
while(True):
	# generating hexagonal numbers
	hex = i * (2 * i - 1)
	# checking if pentagonal
	if is_pent(hex):
		print(hex)
		break

	i += 1


end = time()
print(int((end-start)*1000), "ms")
