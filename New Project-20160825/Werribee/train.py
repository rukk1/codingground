station_list = ['Flinders Street', 'Southern Cross', 'North Melbourne', 'Footscray', 'Seddon']


def train(train_station):
    error = True

    while error == True:
        print '\nWhere are you travelling to?'
        print 'Enter List for list of stations.'
        travelling_to = raw_input('> ')
        #slist = '' #unsure what these did
        #slist_num = -1

        if travelling_to == train_station:
            print "Can't travel to the same place, dummy."
            raw_input()
            error = True
        elif travelling_to == '':
            print "Type something, gosh."
            raw_input()
            error = True
        elif travelling_to == 'List':
            print "List of stations are:"
            
            for items in station_list:
                print(items)
            
            raw_input()
            error = True
        elif travelling_to in station_list:
            error = False
        else:
            print "Fat fingers."
            raw_input()
            error = True

    #what does this do?
    """
    while slist != travelling_to:
        slist_num += 1
        slist = station_list[slist_num]
    """
    
    print "On our way to %s." % travelling_to
    #travel(train_station,travelling_to) #need to create it
    return travelling_to
    
    
#returned = train('Flinders Street') #debugging
#print 'the return value is', returned #debugging