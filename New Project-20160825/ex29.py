people = 20
cats = 30
dogs = 15


if people < cats:
    print "Too many cats!  The world is doomed!"
    
if people > cats:
    print "Not many cats!  The world is saved!"

if people < dogs:
    print "The world is drooled on!"
    
if people > dogs:
    print "The world is dry!"
    
    
    
dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."
    
if people <= dogs:
    print "People are less than or equal to dogs."
    
    
if people == dogs:
    print "People are dogs."
    
# Extra stuff
if (dogs == people and (not (cats > dogs and dogs < people))) != (people != dogs):
    #[true and (not (true and false = false) true)] true != false
    print "This means true isn't false"
    
    