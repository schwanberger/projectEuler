# Number spiral diagonals: https://projecteuler.net/problem=28
# Problem 28 
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
# 
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# 
# It can be verified that the sum of the numbers on the diagonals is 101.
# 
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

'''
The diagonal going from bottom left corner to top right corner follows a pattern.
From center to bottom left corner: num = n^2 + 1 for even n: n = 2, 4, 6 ...
From center to top right corner: num = n^2 for uneven n: n = 3, 5, 7 ...
'''

diagTopRight = (i * i for i in xrange(3, 1001 + 1, 2))
diagBtmLeft = (i * i + 1 for i in xrange(2, 1001 + 1, 2))
diagTopLeft = (i * i - i + 1 for i in xrange(3, 1001 + 1, 2))
diagBtmRight = (i * i - i + 1 for i in xrange(2, 1001 + 1, 2))

print 1 + sum(diagTopRight) + sum(diagBtmLeft) + sum(diagTopLeft) + sum(diagBtmRight)
