import math

def getPrime(num):
    count = 1
    for i in range(3,10000000,2):
        flag=0
        #check for prime
        for j in range(2, int(math.sqrt(i))+1):
            if i%j==0:
                flag=1

        if flag==0:
            count+=1

        # check for range
        if count > num-1:
            return i


#call getPrime function for nth prime
print(getPrime(100001))
