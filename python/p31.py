# -*- encoding: utf-8 -*-

# Coin sums: https://projecteuler.net/problem=31
# Problem 31 
# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
# 
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
# 
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?


def memoize(f):
    memo = {}

    def helper(n, m):
        if (n, m) not in memo:            
            memo[n, m] = f(n, m)
        return memo[n, m]

    return helper


coins = [1, 2, 5, 10, 20, 50, 100, 200]

#Dynamical programming, top-down approach by analysing sub-structure and formulating a recursion that fits
@memoize
def recCount(n, m):
    if n < 0 or m < 0:
        return 0
    if n == 0:  
        return 1
 
    return recCount(n, m - 1) + recCount(n - coins[m], m)


print recCount(200, 7)

#Dynamical programming, iterative bottom up approach derived from recursion above.
def iteCount(n):
    count = [0] * (n + 1)
    count[0] = 1
    for i in xrange(len(coins)):
        for j in xrange(coins[i], n + 1):
            count[j] += count[j - coins[i]]
            
    return count[n]


print iteCount(200)
print iteCount(10000)
