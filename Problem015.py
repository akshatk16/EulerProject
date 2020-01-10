# ?path in a grid from top left to bottom right by moving only down and right
# using combinatorics, we can see that the number of paths is given by n choose k where k is the size of grid and n is 2 times k


from math import factorial
import time

start=time.time()

grid_size=20

def n_choose_k(k):
    res=factorial(2*k)//(factorial(k)*factorial(k))
    print(res)

n_choose_k(grid_size)

end=time.time()
print(end-start)
