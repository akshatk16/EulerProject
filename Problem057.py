# In the first one-thousand expansions of continued fraction representation of
# sqrt(2), how many fractions contain a numerator with
# more digits than the denominator?


# if p/q is the kth expansion
# then the next would be
# 1 + (1 / 1 + (p / q))
# = 1 + (1 / ((q + p) / q))
# = 1 + (q / (p + q))
# = (p + 2q)/(p + q)
#
# thus, for k+1th expansion
# p_k+1 = p_k + 2q_k
# q_k+1 = p_k +q_k


from time import time


start = time()

# initial conditions
p = 1
q = 1
count = 0

for i in range(1000):
	# new numerator and denominator pair
	next_p = p + 2 * q
	next_q = p + q

	# check condition
	if len(str(next_p)) > len(str(next_q)):
		count += 1

	# assign p and q for next iteration
	p = next_p
	q = next_q

print(count)

end = time()
print(int((end-start)*1000), "ms")
