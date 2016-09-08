#import player, currency

welcome_text = """
Welcome to Werribee Line: The Game.  Here you will be tested on your ability to fight your way down the train line, 
barter ciggies for your safety and ultimately defeat the final boss at the end of the line.  Each station has a land mark with 
different foes, each foe having a strength.  You will need luck on your side to best these foes, because - let's face it - 
everyone on the Werribee line is a cunt.
\nYou start with 15 hit points, 15 attack, 15 defence, and 15 ciggies.  Your stats will increase as you win fights and will have a 
chance to find ciggies along the way.  The more fights you win, the smaller the gap between your enemies and yourself becomes.\n
All inputs are case sensitive, hit enter to continue when the text pauses, and most importantly show these fucking pricks who rules this line."""

welcome_text2 = """
You're on the way home from working at Nandos.  It's a shit job, but hey you're a shit person.  
If you weren't, you wouldn't live on the Werribee line with the rest of the scumbags.\n
You find yourself standing on the Flinders St steps, emo kids swarm around your ankles, shielding their eyes with emaciated forearms from the muted Melbourne sunlight."""

return_text = """
Beaten by some shit bag, robbed of your ciggies, battered and bruised.  You fucked up, you should feel bad because you are bad.
Back to Flinders, don't fucked it up again."""

line = "_____________________________________________________________________________________________________________"


def start(newgame):
    if newgame == True:
        print line 
        print welcome_text
        raw_input()
        print line
        print welcome_text2
        return [15, 15, 15, 15]
    else:
        print return_text
        print line