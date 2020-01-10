#sum even fibonacci numbers upto 4,000,000


a, b = 0, 1
sum=0
while b<4000000:
    if b%2 == 0:
        #adding only even values
        sum += b
    a, b = b, a+b
    #fib: a_n+1 = a_n + a_n-1
print(sum)
