# no of ways to obtain a required amount using given set of coins

from time import time


start = time()

required_amount = 200

denominations = [1, 2, 5, 10, 20, 50, 100, 200]
# all possible change denominations in pence

# base condition, to make required_amount 0, we have 1 combination only
combinations = [1] + [0] * required_amount


for val in denominations:
	# all possible denominations
	for i in range(val, required_amount+1):
		# dynamically calculating ways to get current val using current and smaller coins
		combinations[i] += combinations[i-val]

print(combinations[required_amount])


end = time()
print(int((end-start)*1000), "ms")
