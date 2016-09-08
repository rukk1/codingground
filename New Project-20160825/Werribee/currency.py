def currency(current, adjust):
    calculation = (current + adjust)
    if calculation >= 0:
        current += adjust
        return current
    elif calculation < 0:
        return False
    else:
        print 'Error with currency calculation'
        return False

#money = 15
#print 'money', money
#print 'after proc', currency(money, -16) #debugging