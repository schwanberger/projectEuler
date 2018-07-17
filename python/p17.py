from num2words import num2words

def letterCountAlphaNumeric(num):
    return sum(1 for i in num2words(num) if i.isalpha())

print sum(letterCountAlphaNumeric(i) for i in xrange(1,1001))
