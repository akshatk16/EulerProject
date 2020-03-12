# Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
#
# A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
#
# For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.
#
# Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
#
# Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.


from time import time


start = time()


def decrypt(msg, key):
	# simple program to XOR ciphertext with key
	decrypted = []
	for i in range(0, len(msg)):
		temp = msg[i] ^ ord(key[i % len(key)])  # bitwise XOR
		decrypted.append(chr(temp))
	return decrypted


def decrypt_key(msg):
	key = [0]*3
	# count = [0]*100
	# for i in msg:
	# 	count[i] += 1
	# # print(count)
	#
	# record, i = 0, 0
	#
	# # finding most frequent character
	# for i in range(100):
	# 	if count[i] > record:
	# 		record = count[i]
	# 		ind = i
	# # assuming most frequent letter is ' '
	# key_letter = ind ^ ord(' ')
	# ' ' first appears at third position so it must be third letter in key
	key[2] = ord('p')

	# Since third character in ciphertext is a space, the first two characters can only have limited probables. It can either be a two letter word or a letter followed by punctuation mark.

	# for j in range(97, 122):
	# 	for k in range(97, 122):
	# 		temp_key = chr(j) + chr(k)
	# 		t = decrypt(msg[0:2], temp_key)

			# check possible combinations that give two letter words:
			# if ord(t[0]) in range(65, 91) and ord(t[1]) in range(97, 123):
			# 	print(t, chr(j), chr(k), chr(key[2]))

			# The most common two-letter words are of, to, in, it, is, be, as, at, so, we, he, by, or, on, do, if, me, my, up, an, go, no, us, am. Out of these, only An can be a possible starting word and gives a meaningful key, exp

	key[0] = ord('e')
	key[1] = ord('x')
	return key


f = open('p059_cipher.txt')  # open file
t = f.read().strip().split(',')  # remove commas and turn to list
# t = t.strip().split(',')
msg = [int(x) for x in t]  # convert str to int
# print(msg)


key_list = decrypt_key(msg)  # find key
key = ''
for i in key_list:
	key += chr(i)

decrypted_text = ''
sum = 0

temp = decrypt(msg, key)
for i in temp:
	decrypted_text += i
	sum += ord(i)
print(decrypted_text)
print(sum)


end = time()
print(int((end-start)*1000), "ms")
