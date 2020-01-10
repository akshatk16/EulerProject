#pythagorean triple a,b,c where a+b+c=1000


#
# using Euclid's parametric formula
#                     a = m*m - n*n
#                     b = 2*m*n
#                     c = m*m + n*n
# we can see that a + b + c = 2*m*m + 2*m*n


for m in range(1,1000):
    for n in range(1,m):
        res = 2*m*m + 2*m*n
        if res == 1000:
            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n
print(a,b,c)
