# Sum of numbers that are paindromes in both base 10 and 2


from time import time


start = time()


N = 1000000


def chk_palindromic(num):
	digits = [int(x) for x in str(num)]
	if digits == digits[::-1]:  # digits == reverse(digits)
		return True


def chk_bin_palindromic(num):
	bin_num = format(num, '0b')
	if(chk_palindromic(bin_num)):
		return True


sum = 0
for i in range(N):
	if(chk_palindromic(i) is True):
		if(chk_bin_palindromic(i) is True):
			sum += i

print(sum)

end = time()
print(int((end-start)*1000), "ms")
