# -*- encoding: utf-8 -*- 
# 1000-digit Fibonacci number: https://projecteuler.net/problem=25
# Problem 25 
# The Fibonacci sequence is defined by the recurrence relation:
# 
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
# 
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
# 
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?



def fibonacci(limit):
    a = 1
    b = 2
    while a < limit:
        yield a
        a, b = b, a + b

fiboList = list(i for i in fibonacci(11**999))

for index, item in enumerate(fiboList):
    if len(str(item)) == 1000:
        print index+2
        break

#Added 2 to index to align with problem definition of terms (i.e adjusting for the offset)
