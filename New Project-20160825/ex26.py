def break_words(stuff):
    """This function will break up words for us."""
    words_funct = stuff.split(' ')
    #print "printing words from function: ", words #debugging
    return words_funct

def sort_words(words):
    """Sorts the words."""
    #print "words pre split: ", words #debugging
    #sorted = words.sort() #added sorting logic
    #print "words post split: ", sorted
    #return sorted
    #print "Words_func = ", words_func
    #print "Words_func post sort = ", words_func
    #print "words post split: ", words
    return sorted(words)

def print_first_word(words): #added colon
    """Prints the first word after popping it off."""
    word = words.pop(0) #changed poop to pop
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) #added bracket
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

""""
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = \""" #remove slash
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion 
\n\t\twhere there is none.
\""" #changed explntion to explanation (remove slash)


print "--------------"
print poem
print "--------------"

five = 9 - 2 + 3 - 5 #changed 10 to 9
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000 #changed \ to /
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) #changed == to =, changed -point to _point

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point) #changed crabapples to crates, added bracket, changed _pont to _point
"""

sentence = "All good things come to those who wait." #changed god to good, removed tab, weight to wait
words = break_words(sentence) #removed ex25 to call functions from this script
print "Words: %s" % words #debugging
sorted_words = sort_words(words) #removed ex25 to call functions from this script
#print "Sentence: %s" % sentence #debugging
print "Words: %s" % words #debugging
print "Sorted: %s" % sorted_words #debugging

print_first_word(words) #this should return all
print_last_word(words) #this should return wait
print_first_word(sorted_words) #removed . from the start of line (should return all)
print_last_word(sorted_words) #this should return who
sorted_words = sort_sentence(sentence) #removed ex25 to call functions from this script

print sorted_words #changed prin to print (should return list of words)
print_first_and_last(sentence) #changed _irst to _first
print_first_and_last_sorted(sentence) #removed indent, changed _a to _and, changed senence to sentence