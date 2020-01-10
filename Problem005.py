#smallest number divisible by all natural numbers upto 20


def gcd(a,b):
    while(b):
        a,b=b,a%b
    return a


num=[]

for i in range (1,21):
    num.append(i)

lcm=num[0]
for i in num[1:]:
    lcm=int(lcm*i/gcd(lcm,i))
    #lcm(a,b)=a*b/gcd(a,b)

print(lcm)
