# The first known prime found to exceed one million digits was discovered in 1999,
# and is a Mersenne prime of the form 26972593−1; it contains exactly 2,098,960 digits.
# Subsequently other Mersenne primes, of the form 2p−1, have been found which contain more digits.
#
# However, in 2004 there was found a massive non-Mersenne prime which contains
# 2,357,207 digits: 28433×27830457+1.
#
# Find the last ten digits of this prime number.


from time import time


start = time()

target_m = 28433  	# multiplicand
target_p = 7830457  # exponent
n = 10  			# digits required
mod = 10 ** n  		# modulo


# powers of 2, mod 10, follow a pattern of length 4, starting at 2^1 (2,4,8,6,2,4…)
# powers of 2, mod 100, follow a pattern of length 20, starting at 2^2 (04,08,16,32,64,28,56,12,24,48,96,92,84,68,36,72,44,88,76,52,04,08,16…)
# powers of 2, mod 1000, follow a pattern of length 100, starting at 2^3 similarily
# powers of 2, mod 10^n, follow a pattern of length 4 * 5 ^ (n - 1), starting at 2^n

length = 4 * 5 ** (n - 1)  # length of chain


rem = target_p % length  # exponent's position in modulus chain

# computing the product
sol = (2 ** rem) % mod
sol *= target_m
sol %= mod
sol += 1

print(sol)

end = time()
print(int((end-start)*1000), "ms")
