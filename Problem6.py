#difference between square of sum and sum of squares upto a given number


n=100
#square of sum
sum=0
for i in range (1,n+1):
    sum+=i
sum*=sum

#sum of squares
sum1=int(n*(2*n+1)*(n+1)/6)

#difference
dif = sum-sum1
print(dif)
