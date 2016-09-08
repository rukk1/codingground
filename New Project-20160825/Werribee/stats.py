import random

player_hp = 15
player_att = 15
player_def = 15

def stats(hp,att,defence):
    global player_hp, player_att, player_def
    mob_hp = (player_hp + hp)
    percent = (random.randrange(15) * mob_hp) / 100 #calculates a random % up to 15%
    if random.randrange(2) == 1:
        mob_hp -= percent
    else:
        mob_hp += percent
    
    mob_att = (player_att + att)
    percent = (random.randrange(15) * mob_att) / 100 #calculates a random % up to 15%
    if random.randrange(2) == 1:
        mob_att -= percent
    else:
        mob_att += percent
    
    mob_def = (player_hp + defence)
    percent = (random.randrange(15) * mob_def) / 100 #calculates a random % up to 15%
    if random.randrange(2) == 1:
        mob_def -= percent
    else:
        mob_def += percent
    return [mob_hp, mob_att, mob_def]
    
    
print stats(3,1,1)