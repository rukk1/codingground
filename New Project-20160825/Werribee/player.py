player_hp = 0
player_att = 0
player_def = 0

def player(hp,attack,defence):
    global player_hp, player_att, player_def
    player_hp += hp
    player_att += attack
    player_def += defence
   
# testing    
#player(15,15,15)
#print "Starting HP:", player_hp, "Attack:", player_att, "Defence:", player_def
#player(0,-5,1)
#print "Adjusted HP:", player_hp, "Attack:", player_att, "Defence:", player_def