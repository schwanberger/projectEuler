# Sum square difference: https://projecteuler.net/problem=6
# Problem 6 
# The sum of the squares of the first ten natural numbers is,
# 
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# 
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# 
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def sumofSquares(limit):
    result = 0
    for i in xrange(1, limit + 1):
        result += i ** 2
    return result


def sumSquared(limit):
    result = 0
    for i in xrange(1, limit + 1):
        result += i
    return result ** 2


print sumSquared(100) - sumofSquares(100)

