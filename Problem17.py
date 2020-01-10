# counting total number of letters used to write all numbers upto 1000 in british english

from time import time

start=time()

words={#dictionary defining numbers with number of letters in their english equivalent.
       #All numbers can be constructed using the below numbers
    0:0,
    1:3,
    2:3,
    3:5,
    4:4,
    5:4,
    6:3,
    7:5,
    8:5,
    9:4,
    10:3,
    11:6,
    12:6,
    13:8,
    14:8,
    15:7,
    16:7,
    17:9,
    18:8,
    19:8,
    20:6,
    30:6,
    40:5,
    50:5,
    60:5,
    70:7,
    80:6,
    90:6,
    100:7,
    1000:8
}

sum_final=[]
def sum_letters(number):
    sum=0
    n=[0,0,0,0]
    for i in range(3,-1,-1):
        n[i]=number%10
        number=number//10
# made array with digits

    if n[0]!=0:
        sum+=words[1000]+words[n[0]]
        #handling numbers over 999

    if n[1]!=0:
        sum+=words[100]+words[n[1]]
        #handling numbers over 99
    if (n[0]!=0 or n[1]!=0) and (n[2]!=0 or n[3]!=0):
        sum+=3
        #checking if 'and' is needed and adding its weight
    if n[2]<2:
        num=n[2]*10+n[3]
        sum+=words[num]
        #handling numbers upto 20

    else:
        sum+=words[n[2]*10]+words[n[3]]
        #handling numbers between 20 and 99

    return sum

sum=0
for i in range(1001):
    sum+=(sum_letters(i))
print(sum)

end=time()
print(end-start)
