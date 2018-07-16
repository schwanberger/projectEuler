# Summation of primes: https://projecteuler.net/problem=10
# Problem 10 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.

import sys
sys.path.append('./eulerhelpers')

from prime import sieve

print sum(sieve(2000000))
