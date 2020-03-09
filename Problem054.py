# The file, poker.txt, contains one-thousand random hands
# dealt to two players.
# Each line of the file contains ten cards (separated by a single space):
# the first five are Player 1's cards and the last five are Player 2's cards.
# You can assume that all hands are valid
# (no invalid characters or repeated cards),
# each player's hand is in no specific order,
# and in each hand there is a clear winner.

# How many hands does Player 1 win?


from time import time
from collections import Counter

start = time()


value = {  # card to number
	'A': 14,
	'K': 13,
	'Q': 12,
	'J': 11,
	'T': 10,
	'9': 9,
	'8': 8,
	'7': 7,
	'6': 6,
	'5': 5,
	'4': 4,
	'3': 3,
	'2': 2,
	'1': 1
	}


strength = {  # number to card
	14: 'A',
	13: 'K',
	12: 'Q',
	11: 'J',
	10: 'T',
	9: '9',
	8: '8',
	7: '7',
	6: '6',
	5: '5',
	4: '4',
	3: '3',
	2: '2',
	1: '1'
	}


def high_card(val):
	highest = 0
	for i in val:
		if i == 'A':
			return 14
		elif i == 'K':
			if 13 >= highest:
				highest = 13
		elif i == 'Q':
			if 12 >= highest:
				highest = 12
		elif i == 'J':
			if 11 >= highest:
				highest = 11
		elif i == 'T':
			if 10 >= highest:
				highest = 10
		elif int(i) > highest:
			highest = int(i)
	return highest


def pairs(val):
	reps = Counter(val) - Counter(set(val))
	pairs = 0
	for i in reps:
		if reps[i] == 1:
			pairs += 1
	if pairs:
		return pairs + 1  # acc to priority: pair = 2, two pair = 3

	return 0


def highest_pair(val):
		# in case both have pairs
		reps = Counter(val) - Counter(set(val))
		reps = reps.keys()
		highest = 0
		for i in reps:
			if value[i] > highest:
				highest = value[i]
		return highest


def three_of_a_kind(val):
	reps = Counter(val) - Counter(set(val))
	for i in reps:
		if reps[i] == 2:
			return 4  # acc to priority: three_of_a_kind = 4

	return 0


def straight(val):
	highest = high_card(val)
	reps = Counter(val) - Counter(set(val))
	if reps or highest < 5:
		return 0
	for i in range(1, 5):
		if strength[highest - i] not in val:
			return 0
	return 5  # acc to priority: straight = 5


def flush(suit):
	if len(set(suit)) == 1:
		return 6  # acc to priority: flush = 6
	return 0


def full_house(val):
	# three_of_a_kind + pair
	if pairs(val) == 2 and three_of_a_kind(val):
		return 7  # acc to priority: full house = 7
	return 0


def four_of_a_kind(val):
	reps = Counter(val) - Counter(set(val))
	for i in reps:
		if reps[i] == 3:
			return 8  # acc to priority: four_of_a_kind = 8
	return 0


def straight_flush(val, suit):
	if straight(val) and flush(suit):
		return 9  # acc to priority: straight flush = 9
	return 0


def royal_flush(val, suit):
	if high_card(val) == 14 and straight_flush(val, suit):
		return 10  # acc to priority: royal flush = 10
	return 0


def get_val_suit(cards):
	hand = cards.split(' ')
	val, suit = [], []
	for i in hand:
		val.append(i[0])
		suit.append(i[1])
	return [val, suit]


poker = open('p054_poker.txt')
games = poker.read()
poker.close()

both_hands = games.strip().split('\n')

hands = []

for i in both_hands:
	p1 = get_val_suit(i[:14])
	p2 = get_val_suit(i[15:])
	hands.append([p1, p2])

count = 0

for i in hands:
	p1_val = i[0][0]
	p1_suit = i[0][1]

	p2_val = i[1][0]
	p2_suit = i[1][1]

	p1_score = 0
	p2_score = 0

	flag = False  # for pairs

	# for player 1 cards
	if pairs(p1_val):
		p1_score = pairs(p1_val)
		flag = True

	if three_of_a_kind(p1_val):
		p1_score = three_of_a_kind(p1_val)
		flag = True

	if straight(p1_val):
		p1_score = straight(p1_val)

	if flush(p1_suit):
		p1_score = flush(p1_suit)

	if full_house(p1_val):
		p1_score = full_house(p1_val)
		flag = True

	if four_of_a_kind(p1_val):
		p1_score = four_of_a_kind(p1_val)
		flag = True

	if straight_flush(p1_val, p1_suit):
		p1_score = straight_flush(p1_val, p1_suit)

	if royal_flush(p1_val, p1_suit):
		p1_score = royal_flush(p1_val, p1_suit)

	# for player 2 cards
	if pairs(p2_val):
		p2_score = pairs(p2_val)
		flag = True

	if three_of_a_kind(p2_val):
		p2_score = three_of_a_kind(p2_val)
		flag = True

	if straight(p2_val):
		p2_score = straight(p2_val)

	if flush(p2_suit):
		p2_score = flush(p2_suit)

	if full_house(p2_val):
		p2_score = full_house(p2_val)
		flag = True

	if four_of_a_kind(p2_val):
		p2_score = four_of_a_kind(p2_val)
		flag = True

	if straight_flush(p2_val, p2_suit):
		p2_score = straight_flush(p2_val, p2_suit)

	if royal_flush(p2_val, p2_suit):
		p2_score = royal_flush(p2_val, p2_suit)

	# highest score wins
	if p1_score > p2_score:
		count += 1

	elif p1_score == p2_score:
		# cards have pairs
		if flag:
			if highest_pair(p1_val) > highest_pair(p2_val):
				count += 1

			elif highest_pair(i[0][0]) == highest_pair(i[1][0]):
				if high_card(i[0][0]) > high_card(i[1][0]):
					count += 1

		# cards do not have pairs
		else:
			if high_card(p1_val) > high_card(p2_val):
				count += 1

print(count)


end = time()
print(int((end-start)*1000), "ms")
