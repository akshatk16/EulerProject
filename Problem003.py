#largest prime factor


import math
num = 600851475143

def recordPrime(num):
    record = -1
    #base condition

    while num%2 == 0:
        record = 2
        num /= 2
    #removed all even factors


    for i in range (3, int(math.sqrt(num))+1, 2):
        #no even factors so skip all evens
        while num%i == 0:
            record = i
            num /= i

    if num > 2:
        record = num
    #check for prime greater than 2

    return int(record)

print(recordPrime(num))
