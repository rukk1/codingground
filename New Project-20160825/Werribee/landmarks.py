def landmarks(station):
    if station == 'Flinders Street':
        return "Young and Jacksons"
    elif station == 'Southern Cross':
        return "Bus Terminal"
    elif station == 'North Melbourne':
        return "the Melbourne Star"
    else:
        return "Error in landmarks"
        
# testing
#train_station = 'North Melbourne'
#landmark = landmarks(train_station)
#print "Arrived at %s, the landmark is %s." % (train_station, landmark)