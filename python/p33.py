# Digit cancelling fractions
# Problem 33 
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# 
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# 
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
# 
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.


def returnTestCases(a, b):
    testCaseList = []
    for i in xrange(1, 10):
        testCase1 = float(int(str(i) + str(a))) / float(int(str(b) + str(i)))
        testCase2 = float(int(str(a) + str(i))) / float(int(str(i) + str(b)))
#         testCase1 = (str(i) + str(a)) + "," + (str(b) + str(i))
#         testCase2 = (str(a) + str(i)) + "," + (str(i) + str(b))
        testCaseList.append(testCase1)
        testCaseList.append(testCase2)

    return testCaseList

matchList = []

for a in xrange(1, 9):
    for b in xrange(a + 1, 10):
        #print a,b
        test = float(a)/float(b)
        testCases = returnTestCases(a, b)
        #print testCases
        for tests in testCases:
            if test == tests:
                matchList.append(test)
        


#print returnTestCases(4, 8)
#print len(returnTestCases(1, 3))
print matchList
print len(matchList)
# 
# print float(4/8) == float(49/98)