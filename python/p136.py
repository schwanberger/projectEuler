# Prime pair connection: https://projecteuler.net/problem=134
# Problem 134 
# Consider the consecutive primes p1 = 19 and p2 = 23. It can be verified that 1219 is the smallest number such that the last digits are formed by p1 whilst also being divisible by p2.
#  
# In fact, with the exception of p1 = 3 and p2 = 5, for every pair of consecutive primes, p2 > p1, there exist values of n for which the last digits are formed by p1 and n is divisible by p2. Let S be the smallest of these values of n.
#  
# Find sum of S for every pair of consecutive primes with 5 <= p1 <= 1000000.

from itertools importproduct, repeat, combinations, combinations_with_replacement
from operator import mul
import sys

from prime import *

sys.path.append('./eulerhelpers')

primeList = []
primeGen = sieve(10 ** 6)
next(primeGen)
 
for prime in primeGen:
     
    primeList.append(prime)

n = 3
while True:
    p1 = 19
    p2 = 23
    
    candidate = p2 * n
    
    if candidate > 1300:
        break
    if int(str(candidate)[-2:]) == 19:
        print "Succes!"
        print candidate
        break
    n += 2

#===============================================================================
# def genNextCList():
#     i = 0
#     while 1:
#         yield 
# 
# def genNextCandidate():
#     i = 0
#     while 1:
#         yield p2*cList[i]
#         i +=1
# 
# 
# nextCandidate = genNextCandidate()
# print next((nextCandidate))
# print next((nextCandidate))
#===============================================================================

#===============================================================================
# b2 = list(combinations_with_replacement([5, 7, 11], 2))
# b3 = list(combinations_with_replacement([5, 7, 11], 3))
# b4 = list(combinations_with_replacement([5, 7, 11], 4))
# b5 = list(combinations_with_replacement([5, 7, 11], 5))
# 
#   
# # print b2
# def getTupleMul(herp):
#     c = []
#     for leTuple in herp:
#         c.append(reduce(mul, leTuple, 1))
#     return c
# 
# 
# print getTupleMul(b2)
# print getTupleMul(b3)
# print getTupleMul(b4)
# print getTupleMul(b5)
#===============================================================================
