#
# Consider quadratic Diophantine equations of the form:
#
# x^2 – Dy^2 = 1
#
# For example, when D=13, the minimal solution in x is 6492 – 13×180^2 = 1.
#
# It can be assumed that there are no solutions in positive integers when D is square.
#
# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
#
# 3^2 – 2×2^2 = 1
# 2^2 – 3×1^2 = 1
# 9^2 – 5×4^2 = 1
# 5^2 – 6×2^2 = 1
# 8^2 – 7×3^2 = 1
#
# Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.
#
# Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.


# The given equation is Pell's equation and the solution requires continued fraction expansion. The solution uses all but last constant in the convergent period

# for odd periods, the equation x^2 – Dy^2 = gives soltuion for -1, for even, 1

# Bhaskar's lemma is used to find required solution for negative Pell's equation
from time import time


start = time()


def continued_fraction(n):
	# Formula for a, m, d from source 2
	a_0 = int(n ** 0.5)

	if a_0 == n ** 0.5:  # perfect square
		return 0

	m_current = 0.0
	d_current = 1.0
	a_next, a_current, convergents = a_0, a_0, [a_0]

	while a_next != 2 * a_0:  # condition for period cycle from source 1
		# computing next iterations
		m_next = (d_current * a_current) - m_current
		d_next = (n - (m_next ** 2)) / d_current
		a_next = int((a_0 + m_next) / d_next)

		# initialising values for next iteration
		m_current = m_next
		d_current = d_next
		a_current = a_next

		convergents.append(a_next)
	return convergents[:-1]


def fractional_form(n):
	nums = 1
	dens = n.pop()
	if n:
		for t in n[::-1]:
			temp = dens
			dens = (t * dens) + nums  # converting mixed fraction to improper form
			nums = temp
		nums = dens
		dens = temp

	return nums, dens


record = 0, 0, 0
for d in range(1, 1001):  # given range
	if d % (d ** 0.5) != 0:
		convs = continued_fraction(d)  # getting the continued fraction
		if len(convs) % 2 != 0:  # existence of solution
			nums, dens = fractional_form(convs)  # converting to improper fraction
			x, y = 2 * nums ** 2 + 1, 2 * nums * dens  # using formula to find solution for x and y
		else:
			x, y = fractional_form(convs)
		if x > record[0]:  # checking for new record
			record = x, d, y  # updating record

print("x^2 - D*y^2 = 1")
print("x = ", record[0])
print("D = ", record[1])
print("y = ", record[2])

end = time()
print(int((end-start)*1000), "ms")
