# Special Pythagorean triplet: https://projecteuler.net/problem=9
# Problem 9 
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def pytTriplet(tripsum):
    for a in xrange(1, tripsum + 1):
        for b in xrange(1, tripsum + 1):
            if a > b:
                continue
            c = (a ** 2 + b ** 2) ** 0.5
            if a + b + c == tripsum:
                return int(a * b * c)


print pytTriplet(1000)       
