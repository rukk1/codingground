import random


def encounter(source,destination):
    # ensures the bigger variable is first to avoid negative number, times 10 to make it a %
    chance = 10 * (max(source, destination) - min(source, destination))
    rng = random.randrange(100)
    if rng > chance:
        return False
    elif rng <= chance:
        return True
    else:
        print "RNG is: %d.  Chance is: %d" % (rng, chance)
        return 'error in encounter'
    
    
chance = encounter(1,5)
print 'Main:', chance