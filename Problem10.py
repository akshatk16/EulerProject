# sum of Primes using Sieve Of Eratosthenes


def getPrimes(n):
    m = (n-1)//2
    nums = [True] * m
    i, p, primes = 0,3,[2]
    while p*p<n:
        if nums[i]:
            primes.append(p)
            j = 2*i*i + 6*i + 3
            while j<m:
                nums[j] = False
                j = j + 2*i + 3
        i+=1
        p+=2
    while i<m:
        if nums[i]:
            primes.append(p)
        i+=1
        p+=2

    return primes


print(sum(getPrimes(2000000)))
