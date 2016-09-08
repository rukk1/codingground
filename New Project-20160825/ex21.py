def add (a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
    
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b
    
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b
    
def divide(a, b):
    print "DIVIDING %d / %d" % ( a, b)
    return a / b
    
    
print "Let's do some match with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age %d, Height, %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

# (100 / 2) / 2 = A (25)
# (90 * 2) * A = B (4500)
# (78 - 4) - B = C (-4426)
# (30 + 5) + C = what (-4391)
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"


# write out formula: 24 + 34 / 100 - 1023
div = divide(34.0, 100.0)
ad = add(24.0, div)
sub = subtract(ad, 1023.0)

write = subtract(add(ad, div), 1023.0)
print "\n%s + 24 - 1023" % div
print "%s - 1023" % ad
print "Write out forumula is: %r" % write