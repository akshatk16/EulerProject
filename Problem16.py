# sum of digits in 2*1000


from time import time

start=time()

print(sum(map(int, str(2**1000))))

end=time()
print(end-start)
