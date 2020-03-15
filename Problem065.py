# Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.

from time import time


start = time()

# generating continued fraction for e
numerators = [1] * 100  # initialising all constants to 1
numerators[0] = 2  # first constant is 2

j = 1  # counter
for i in range(100):
	if i % 3 == 2:  # given series for e
		# e = [2; 1,2,1,1,4,1,1,6,1,...,1,2k,1,...].
		numerators[i] = 2 * j
		j += 1


nums = 1  # initialising numerator
dens = numerators[-1]  # initialising denominator
# starting calculation from bottom of continued fraction
for t in numerators[-2::-1]:
	temp = dens
	dens = (t * dens) + nums  # converting mixed fraction to improper form
	nums = temp

# final iteration inversion to get numerator and denominator
nums = dens
dens = temp

# calculating digit sum
dig_sum = 0
for digits in str(nums):
	dig_sum += int(digits)

print("numerator   = ", nums)
print("denominator = ", temp)
print('')
print("e = ", nums / temp)
print('')
print("sum of digits in numerator = ", dig_sum)


end = time()
print(int((end-start)*1000), "ms")
