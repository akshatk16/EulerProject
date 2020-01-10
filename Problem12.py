import math
import time

start=time.time()

def factorise(num):
    # factorises every number and counts total number of factors
    divisors=[]
    count=0
    while num%2 == 0:
        count+= 1
        num /= 2
    #removed all even factors
    divisors.append(count)

    for i in range (3, int(math.sqrt(num))+1, 2):
        count=0
        #no even factors so skip all evens
        while num%i == 0:
            count+=1
            num /= i
        divisors.append(count)
    # check case for prime over 2
    if num > 2:
        divisors.append(1)

    prod=1

    # total number of factors
    for x in divisors:
        prod*=x+1
    return(prod)
# factorise(28)
prod, n=1,1
RECORD=1
while prod<500:
    # generate nth triangle number
    triangle_number=n*(n+1)//2
    prod=factorise(triangle_number)
    n+=1
    if RECORD<prod:
        RECORD=prod
print(triangle_number, prod)

end=time.time()
print(end-start)
