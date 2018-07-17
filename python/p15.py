# Lattice paths: https://projecteuler.net/problem=15
# Problem 15 
# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# 
# 
# How many such routes are there through a 20x20 grid?


def memoize(f):
    memo = {}

    def helper(i, j):
        if (i, j) not in memo:            
            memo[i, j] = f(i, j)
        return memo[i, j]

    return helper

# Brute runs for more than 15 minutes without memoization


@memoize
def brute(i, j):
    if i > 0 and j > 0:
        return brute(i - 1, j) + brute(i, j - 1)
    
    if i == 0 and j > 0:
        return brute(i, j - 1)
    
    if i > 0 and j == 0:
        return brute(i - 1, j)
    
    if i == 0 and j == 0:
        return 1


for i in xrange(1, 21):
    print i, brute(i, i)
