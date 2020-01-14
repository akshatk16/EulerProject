# Sum of numbers that cant be made using sum of two abundant numbers: number whose sum of divisors exceed itself


from time import time


start = time()

abundant_number = []

pair_sum = []
for i in range(28112):
	pair_sum.append(i)


def abundant_number_gen():
	for i in range(12, 28112):
		# all numbers over 28123 can be constructed using two abundant numbers
		temp = 0
		for j in range(1, i//2 + 1):
			if i % j == 0:
				temp += j
			if temp > i:
				abundant_number.append(i)
				break


abundant_number_gen()

for i in abundant_number:
	for j in abundant_number:
		# numbers that can be constructed using abundant numbers
		k = i+j
		if k < 28112:
			pair_sum[k] = 0
print(sum(pair_sum))

end = time()
print(int((end-start)*1000), "ms")
