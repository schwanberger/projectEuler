# Largest palindrome product: https://projecteuler.net/problem=4
# Problem 4 
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.


def isPalindrome(n):
    s = str(n)
    s1 = s[0:len(s) / 2]
    s2 = s[len(s) - len(s) / 2:]
    return s1 == s2[::-1]


max = 0
for a in xrange(100, 1000):
    for b in xrange(100, 1000):
        c = a * b
        if isPalindrome(c) and c > max:
            max = c
            
print max
