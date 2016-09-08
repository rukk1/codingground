import random
#mob_stats = []
#flavor_text = ''

#added for debugging
player_hp = 25
player_att = 25
player_def = 25

#train_station = 'Flinders Street'


def mob(train_station):
    #global mob_stats, flavor_text
    #mob = random.randrange(1,4)
    #mob = 1 #debugging
   
    if train_station == 'Flinders Street':
        
        if mob == 1:
            #mob_hp, mob_att, mob_def
            flavor_text = "She glances at you, looking straight through you.  You open your mouth to order a drink just as her big meaty paw is wrapped around your throat.\nShe's eaten piece of shit like you for breakfast, brunch and dinner.  Thusly her hit points are higher than usual."
            mob_stats = [5,0,0] 
            return [flavor_text, mob_stats, 'Angry Bartender']
        elif mob == 2:
            flavor_text = "The smell hits you before you notice him huddled in the corner, already intensely staring at you.  He knows he shouldn't be in there, but who are you to tell him otherwise?\nHe loves a good fight and is already approaching you, making fists out of his grubby black hands.\nHe's been kicked up and down Swanston Street during his life, therefore his defense his higher than usual."
            mob_stats = [0,0,5]
            return [flavor_text, mob_stats, 'Drunk Homeless Guy']
        else:
            flavor_text = "It's a Wednesday morning, but that didn't stop the loud kid at the bar from buying his first legal drink as soon as he could.\nOf course he walked into the first pub he saw, knowing no better.  He's feeling king of the world, he just finger banged Katie Dunn on the train in and is feeling unstoppable.\nHe's sizing you up, eager to prove his newly found manhood.  Being young he's quick and hits hard, reflected in higher than usual attack."
            mob_stats = [0,5,0]
            return [flavor_text, mob_stats, 'Kid on His 18th Birthday']
            
    elif train_station == 'Train':
        
        if mob == 1:
            flavor_text = "An Indian middle aged woman approaches you, squaring you up and boxing you into the section of seats that you're in.\n'Tickets, please!'  She says with a sadastic smile, her lips curling back.  You can tell that this is going to go badly whether you can produce a valid ticket or not.\nShe's been working Werribee line for 5 years and shrugs off trolley poles to the face with the best of them, her defense is higher than usual."
            mob_stats = [0,0,5]
            return [flavor_text, mob_stats, 'Ticket Inspector'] 
        elif mob == 2:
            flavor_text = "You hear a clatter happening down the carriage.  You glance up to see a sea of little chubby arms and legs enveloping a just as chubby stocky woman with a mullet.\n'JAYDEN' she screams 'NO FUCKING CHEETOS UNTIL YOU'VE FINISHED YOUR MACCAS.'  You lock eyes with her, you cannot turn away out of sheer disgusted curiosity.\n'WHAT ARE YOU LOOKING AT, CUNT?' She puts to you.  You start to stammer a response just as she lunges at you.\nThis old girl can go all day (or night), her hit points are higher than usual."
            mob_stats = [5,0,0]
            return [flavor_text, mob_stats, 'Mother With a Stroller']
        else:
            flavor_text = "As if my magic a stringy sickly looking guy appears in the seat directly opposite you.  He asks to use your phone, you politely decline.\nHe seems pretty insitant on using your phone, you realise this as he puts his knee into your throat.\nAlthough nothing but skin and bones, this junkie can throw down with the best of them.  His attack is higher than usual."
            mob_stats = [0,5,0]
            return [flavor_text, mob_stats, 'Junkie Wearing Monster cap']
            
    elif train_station == 'Southern Cross':
        
        if mob == 1:
            flavor_text = "A blonde haired kid with a giant bag on his back is making his way through the crowd.  You see a Canadian flag on his pack, but by the way he struts around you can tell he's American (probably a Trump voter too).  He obviously has no idea where he's going, scratching his head, constantly darting this way and that trying to get people's attention.  'Excuse me, brah, can you tell me where the nearest Mickey D's is?'  You let out a chuckle at the overall preposterousness of him, he takes it as an attack on his first amendment rights and flies into a blind rage.  He took an MMA class last summer with his bro Chad, therefore his attack is higher than usual."
            mob_stats = [5,0,0]
            return [flavor_text, mob_stats, 'Lost Backbacker'] 
        elif mob == 2:
            flavor_text = "A man in a (synthetic blend) suit is charging towards you, not at you, but he means to get through you.  You both get stuck into that stupid left/right dance.  He quickly loses patiences and screams \"I've got deliverables to deliver.  Do the needful and move!\" You both step the same way again and he loses his patience, making a fist with one hand, shielding himself with his briefcase in the other hand.  Because of his shield his defence is higher than normal."
            mob_stats = [0,0,5]
            return [flavor_text, mob_stats, 'Business Guy in a rush']
        else:
            flavor_text = "A wrong-side-of 50 fat man in a high vis vest and a 'silly' hat jumps out at you.  'Big Issue, support the homeless' he growls at you.  You fumble for change but come up dry.  This enrages him as he drops his kit to the ground to deal with you.  All that extra cushion for the pushin' adds to his HP."
            mob_stats = [0,5,0]
            return [flavor_text, mob_stats, 'Surly Big Issue Vendor']


def stats(p_hp,p_att,p_def,m_hp,m_att,m_def):
    
    mob_hp = (p_hp + m_hp)
    percent = (random.randrange(15) * mob_hp) / 100 #calculates a random % up to 15%
    
    if random.randrange(2) == 1:
        mob_hp -= percent
    else:
        mob_hp += percent
    
    mob_att = (p_att + m_att)
    percent = (random.randrange(15) * m_att) / 100 #calculates a random % up to 15%
    
    if random.randrange(2) == 1:
        mob_att -= percent
    else:
        mob_att += percent
    
    mob_def = (p_hp + m_def)
    percent = (random.randrange(15) * mob_def) / 100 #calculates a random % up to 15%
   
    if random.randrange(2) == 1:
        mob_def -= percent
    else:
        mob_def += percent
    
    return [mob_hp, mob_att, mob_def]


def mob_text(mob_name, mob_hp, mob_att, mob_def, p_hp, p_att, p_def, flavor_text, train_fight):
    
    if train_fight == True:
        print "While travelling on the train you sense you are in danger..."
        raw_input()
        
    print "You've encountered %s, with %d hit points, %d attack and %d defence.\nYou have %d hit points, %d attack and %d defence.\n\n%s" % (mob_name, mob_hp, mob_att, mob_def, p_hp, p_att, p_def, flavor_text)
    raw_input()


#debugging
#mob_name = mob('Train')
#mob_text()