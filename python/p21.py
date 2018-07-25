# -*- encoding: utf-8 -*-
# Amicable numbers: https://projecteuler.net/problem=21
# Problem 21 
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# 
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# 
# Evaluate the sum of all the amicable numbers under 10000.


def sumProperDiv(n):
    result = 0
    for x in xrange(1, int(n * 0.5) + 1):
        if n % x == 0:
            result += x

    return result

amicableSum = 0
listNandFN = []

for i in xrange(1,10001):
    sortedNandFN = sorted((i,sumProperDiv(i)))
    if sortedNandFN in listNandFN:
        amicableSum += sum(sortedNandFN)
        print "Hit!", sortedNandFN
    listNandFN.append(sortedNandFN)
     
print amicableSum