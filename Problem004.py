#largest palindrome that is product of two 3 digit numbers


def checkPalindrome(num):
    new=0
    temp=num

    while temp>1:
        new = new*10 + temp%10
        #reversing the number
        temp=int(temp/10)


    if new == num:
    #check if number and reverse are equal, hence palindrome
        return True

    return False


record = 1
for i in range (999,100,-1):
    for j in range (999,100,-1):
        prod=i*j
        if record < prod:
            if checkPalindrome(prod):
                record, a, b = prod, i, j

print(record, "=", a, "*", b)
