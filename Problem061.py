from time import time


start = time()
numbers = []


# generating lists of figurate numbers with 4 digits
triangular = [n*(n+1)//2 for n in range(45, 141)]
square = [pow(n, 2) for n in range(32, 100)]
pentagonal = [n*(3*n-1)//2 for n in range(26, 82)]
hexagonal = [n*(2*n-1) for n in range(23, 71)]
heptagonal = [n*(5*n-3)//2 for n in range(21, 64)]
octagonal = [n*(3*n-2) for n in range(19, 59)]

# generating tuples of each 4 digit number split into 2 digits
triangular_tuple = [(x//100, x - (x//100)*100) for x in triangular]
square_tuple = [(x//100, x - (x//100)*100) for x in square]
pentagonal_tuple = [(x//100, x - (x//100)*100) for x in pentagonal]
hexagonal_tuple = [(x//100, x - (x//100)*100) for x in hexagonal]
heptagonal_tuple = [(x//100, x - (x//100)*100) for x in heptagonal]
octagonal_tuple = [(x//100, x - (x//100)*100) for x in octagonal]


# list of all figurate numbers except octagonal numbers
figs_3_to_7 = [heptagonal_tuple, hexagonal_tuple, pentagonal_tuple, square_tuple, triangular_tuple]

# figuate1 is octagonal tuples
for figurate2 in figs_3_to_7:
	# print(1)
	for n1 in octagonal_tuple:
		# print(2)
		for n2 in figurate2:
			# print(1)
			if n1[1] == n2[0]:  # checking cyclicity
				# print(2)
				for figurate3 in figs_3_to_7:
					# print(1)
					if figurate3 != figurate2:  # checking repetition
						# print(2)
						for n3 in figurate3:
							# print(1)
							if n2[1] == n3[0]:  # checking cyclicity
								# print(2)
								for figurate4 in figs_3_to_7:
									# print(1)
									if (figurate4 != figurate3 and figurate4 != figurate2):  # checking repetition
										# print(2)
										for n4 in figurate4:
											# print(1)
											if n3[1] == n4[0]:  # checking cyclicity
												# print(2)
												for figurate5 in figs_3_to_7:
													# print(1)
													if (figurate5 != figurate4 and figurate5 != figurate3 and figurate5 != figurate2):  # checking repetition
														# print(2)
														for n5 in figurate5:
															# print(2)
															if n4[1] == n5[0]:  # checking cyclicity
																# print(1)
																for figurate6 in figs_3_to_7:
																	# print(2)
																	if (figurate6 != figurate5 and figurate6 != figurate4 and figurate6 != figurate3 and figurate6 != figurate2):  # checking repetition
																		# print(1)
																		for n6 in figurate6:
																			# print(2)
																			if n6[0] == n5[1] and n6[1] == n1[0]:  # checking cyclicity
																				# print(1)
																				numbers = [n1, n2, n3, n4, n5, n6]

total = 0
for num in numbers:
	total += num[0]*100+num[1]
print(total)


end = time()
print(int((end-start)*1000), "ms")
