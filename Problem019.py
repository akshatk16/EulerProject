days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# print(days[])

day = 0  # Tuesday
sundays = 0

for year in range(1901, 2001):
	if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
		days[1] = 29
	else:
		days[1] = 8
	for d in range(12):
		day += days[d]
		if day % 7 == 5:  # Sunday
			sundays += 1

print(sundays)
