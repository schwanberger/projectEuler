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


# brutus runs for more than 15 minutes without memoization
@memoize
def brutus(i, j):
    if i > 0 and j > 0:
        return brutus(i - 1, j) + brutus(i, j - 1)
    
    if i == 0 and j > 0:
        return brutus(i, j - 1)
    
    if i > 0 and j == 0:
        return brutus(i - 1, j)
    
    if i == 0 and j == 0:
        return 1

print brutus(20,20)
