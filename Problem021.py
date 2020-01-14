sumF = []


def sum_pair(num, chk):
	sum = 0
	for i in range(1, num):
		if num % i == 0:
			sum += i
	if sum == chk:
		sumF.append(num)
		sumF.append(chk)


def sum_divisors(num):
	sum = 0
	for i in range(1, num):
		if num % i == 0:
			sum += i
	if sum != num:
		sum_pair(sum, num)


for i in range(10000):
	sum_divisors(i)
print(sum(sumF)//2)
