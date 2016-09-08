import start, explore, mobs, currency, combat, train, travel                                   #imports functions
#player set to 15hp, 15att, 15def, 15 ciggies
player_hp, player_att, player_def, money = start.start(True)                       #sets starting money, stats, and prints starting flavor text
dead = False
fight = False
start = False
battled = True
train_fight = False
travelling_to = 'Flinders Street'
train_station = 'Flinders Street'
line = "_____________________________________________________________________________________________________________"

#todo
    
#TO DONE
    #move 'welcome to station' from travel to 'check out landmark'
    #add a flee function
        #decided not to, it's working as is
    #see if you can remove more code from main into victory()
        #decided not to, it's working as is
    
#bugs    

#FIXED
    #check out landmarks or back to train? welcome to train?
        #fixed by adding battled to skip train(), so it goes straight to explore(travelling_to)
    #fleeing during train fight takes us back to origin
        #fixed by passing flee travelling_to and assigning it back to train_station (which was 'train')
    #fix turn in combat, player always goes first regardless
        #turn was either 1 or 0, meaning that 0 wasn't always the first turn.  changed fight_turn to static 0

while True:
    if dead == True:
        start.start(False)
        print '\nYou have %d HP, %d att, %d def and %d ciggies.' % (player_hp, player_att, player_def, money)
        raw_input()
        dead = False
    if start == True: #runs the first time to skip travel
        train_fight = False
        travelling_to = train_station
        start = False
    elif battled == False:
        travelling_to = train.train(train_station)
        train_fight = travel.travel(train_station, travelling_to)
        battled = True
    else:
        if train_fight == True:
            fight = train_fight
            train_station = 'Train'
        else:
            train_station = travelling_to
            fight, train_station, landmark = explore.explore(train_station)                      #returns station/landmark name if player chooses not to fight, False if not
            battled = False
    
    while fight == True:                                                       #meaning player chose to fight
        flavor_text, mob_bonus, mob_name = mobs.mob(train_station)                     #gets text, bonus and name of mob
        mob_hp, mob_att, mob_def = mobs.stats(
            player_hp, player_att, player_def,
            mob_bonus[0], mob_bonus[1], mob_bonus[2])    #creates mob stats (player stats + bonus) with a 15% variance
        print line
        mobs.mob_text(
            mob_name, mob_hp, mob_att, mob_def, player_hp, 
            player_att, player_def, flavor_text, train_fight) #prints mob/player stats with text
        flee, train_station = explore.fight(train_station, travelling_to)                                                  #asks if the player wants to fight the newly created mob

        if flee == True:
            ciggies = currency.currency(money, -5)                                  #if player wants to flee, it tries to minus 5 currency
            if ciggies == False:                                                #if deducted amount is greater than current ciggies, returns False
                print 'Not enough ciggies, you gotta fight %s.' % mob_name
                raw_input()
                fight = True
                flee = False #unsure if this will go back to start in if loop?
            else:                                                            #able to deduct ciggies and avoid fight
                money = ciggies
                print "%s grunts and accepts the 5 ciggies, you now have %d ciggies left." % (mob_name, money)
                battled = True
                train_fight = False
                fight = False                                                  #exists loop, goes onto ????
        else:
            alive, loot, money = combat.combat(player_hp, player_att, player_def, mob_hp, mob_att, mob_def, mob_name, money)
            if (alive == True) and (loot > 0):
		   	    level_hp, level_att, level_def = combat.victory()
		   	    player_hp += level_hp
		   	    player_att += level_att
		   	    player_def += level_def
		   	    money += loot
		   	    print "\nYou gained %d HP, %d attack, %d defence.  Your stats are now: %d HP, %d ATT, %d DEF." % (level_hp, level_att, level_def, player_hp, player_att, player_def)
		   	    print "You found %d ciggies on the crumpled corpse of %s.  Now you have %d." % (loot, mob_name, money)
		   	    battled = True
		   	    train_fight = False
		   	    fight = False
            elif (alive == True) and (loot == 0):
                print 'You lose nothing but the respect of %s.' % mob_name
                fight = False
            elif alive == False:
                ciggies = currency.currency(money, -5)
                if ciggies == False:
                    player_hp -= 5
                    player_att -= 5
                    player_def -= 5
                    money /= 2
                    print "Not enough ciggies to convince the ambo's to fix you up.  Back to the start for you!  You get rolled for half your ciggies and lose 5 to all stats."
                    fight = False
                    dead = True
                else:
                    print "You gave the ambo's 5 ciggies to fix you up.  They dump you at the train station.  You have %d ciggies left." % money
                    battled = False
                    train_fight = False
                    fight = False
                    #need to exit the loop and return to train station using current station