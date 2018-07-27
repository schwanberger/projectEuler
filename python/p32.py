# -*- encoding: utf-8 -*-
# Pandigital products
# Problem 32 
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# 
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# 
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# 
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

from itertools import permutations

matchSet = set()

perm4List = [int(''.join(num)) for num in list(permutations('123456789', 4))]

print perm4List

print sorted('5621' + '8')
print sorted('123458679')

for num in perm4List:
    for a in xrange(1, 10):
        for b in xrange(1000, 10000):
            if a * b == num and sorted(str(a) + str(b) + str(num)) == sorted('123456789'):
                matchSet.add(num)
                
for num in perm4List:
    for a in xrange(10, 100):
        for b in xrange(100, 1000):
            if a * b == num and sorted(str(a) + str(b) + str(num)) == sorted('123456789'):
                matchSet.add(num)
                
print matchSet
print sum(matchSet)
