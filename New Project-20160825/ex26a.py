def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    #print "printing words from function: ", words #debugging
    return words

def sort_words(words_var):
    """Sorts the words."""
    #print "words pre split: ", words #debugging
    #sorted = words.sort() #added sorting logic
    #print "words post split: ", sorted
    #return sorted
    #stuff = words.sort()
    print "words post split: ", words_var
    print func_string
    sorts = words.sort()
    print "function sent ", sentence
    print "Words within function ", words
    print "Sorts within function ", sorts
    return sorts

sentence = "All good things come to those who wait." #changed god to good, removed tab, weight to wait
words = break_words(sentence) #removed ex25 to call functions from this script
#print "Words: %s" % words #debugging
func_string = "hello"
sorted_words = sort_words(words) #removed ex25 to call functions from this script
print "Sentence: %s" % sentence #debugging
#print "Words: %s" % words #debugging
print "Sorted: %s" % sorted_words #debugging

"""
print_first_word(words) #this should return all
print_last_word(words) #this should return wait
print_first_word(sorted_words) #removed . from the start of line (should return all)
print_last_word(sorted_words) #this should return who
sorted_words = sort_sentence(sentence) #removed ex25 to call functions from this script

print sorted_words #changed prin to print (should return list of words)
print_first_and_last(sentence) #changed _irst to _first
print_first_and_last_sorted(sentence) #removed indent, changed _a to _and, changed senence to sentence"""