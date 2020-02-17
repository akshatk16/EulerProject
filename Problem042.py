# number of triangle words in a text file

# if the sum of alphabetical positions of letters in a word is
# a triangle number, the word is a triangle word

from time import time


start = time()

letters = {
				"A": 1,
				"B": 2,
				"C": 3,
				"D": 4,
				"E": 5,
				"F": 6,
				"G": 7,
				"H": 8,
				"I": 9,
				"J": 10,
				"K": 11,
				"L": 12,
				"M": 13,
				"N": 14,
				"O": 15,
				"P": 16,
				"Q": 17,
				"R": 18,
				"S": 19,
				"T": 20,
				"U": 21,
				"V": 22,
				"W": 23,
				"X": 24,
				"Y": 25,
				"Z": 26
			}

# list of first 20 triangle numbers since the largest sum does not exceed t_20
triangle_numbers = [0]*20
for i in range(1, 20):
	triangle_numbers[i] = triangle_numbers[i-1] + i

# reading file content
file = open("p042_words.txt", "r")

# file given with commas as seperators and contain "" around names
words = file.read().replace('"', '').split(',')

# calculating sum
count = 0
for word in words:
	sum = 0
	for letter in word:
		sum += letters[letter]
	if sum in triangle_numbers:
		count += 1

print(count)


end = time()
print(int((end-start)*1000), "ms")
