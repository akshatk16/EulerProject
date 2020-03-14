# How many continued fractions for sqrt(N) for N≤10000 have an odd period?

# Source 1:
# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Algorithm

# Source 2:
# https://www.mathstat.dal.ca/FQ/Papers1/42-2/quartrippon02_2004.pdf


from time import time


start = time()


def continued_fraction(n):
	# Formula for a, m, d from source 2
	a_0 = int(n ** 0.5)

	if a_0 == n ** 0.5:  # perfect square
		return 0

	m_current = 0.0
	d_current = 1.0
	a_next, a_current = a_0, a_0

	period = 0

	while a_next != 2 * a_0:  # condition for period cycle from source 1
		# computing next iterations
		m_next = (d_current * a_current) - m_current
		d_next = (n - (m_next ** 2)) / d_current
		a_next = int((a_0 + m_next) / d_next)

		# initialising values for next iteration
		m_current = m_next
		d_current = d_next
		a_current = a_next

		period += 1

	return period


count = 0
for i in range(10001):
	if continued_fraction(i) % 2 == 1:
		count += 1
print(count)

end = time()
print(int((end-start)*1000), "ms")
