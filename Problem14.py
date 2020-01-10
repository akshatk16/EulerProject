# longest collatz chain under 1000000


import time

start=time.time()


RECORD, MAX=1,1
cache=[0,1]    #stores previously computed values for indices for faster computation
def collatz(n):
    count=1
    num=n
    while n>=num:
        if n%2==1:
            n=(3*n+1)//2
            #skips an iteration as an odd number will turn into an even after a single iteration
            # and thus it is being divided by 2 simultaneously
            count+=2
        else:
            n=n//2
            count+=1
        # print(n, count)

    if(n<num and n>1):
        count+=cache[n]-1
    cache.append(count)
    return count

# print(collatz(5))
for i in range(2,1000001):
    count=collatz(i)
    if RECORD<count:
        RECORD=count
        MAX=i
print(MAX, "takes", RECORD, "steps to reach 1")

end=time.time()
print(int((end-start)*1000),"ms")
