# Digit factorials
# Problem 34 
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# 
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# 
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

from math import factorial

upperBound = 10**7
#upperBound = 12

matchSet = set()

for i in xrange(3,upperBound):
    if sum(factorial(int(digit)) for digit in str(i)) == i:
        matchSet.add(i)
        

print matchSet
print sum(matchSet)