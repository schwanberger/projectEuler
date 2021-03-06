# Longest Collatz sequence: https://projecteuler.net/problem=14
# Problem 14 
# The following iterative sequence is defined for the set of positive integers:
# 
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.

def memoize(f):
    memo = {}

    def helper(n):
        if n not in memo:            
            memo[n] = f(n)
        return memo[n]

    return helper
    
@memoize
def collatzSeq(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        n = n / 2
        return 1 + collatzSeq(n)
    n = 3 * n + 1
    return 1 + collatzSeq(n)


current_max = 0
for i in xrange(1, 1000000):
    seq = collatzSeq(i)
    if seq > current_max:
        current_max = seq
        print i, seq
