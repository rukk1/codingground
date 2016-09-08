#configures argument variable
from sys import argv

#defines variables based on argv
script, filename = argv

#prints filename
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
#opens filename in write mode, defines target variable
target = open(filename, 'w')

#truncates target, deleting contents of file
#print "Truncating the file.  Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."

#defines 3 variables based off string input
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#writes line variables to target variable
target.write("%s \n%s \n%s" % (
    line1, line2, line3))

print "And finally, we close it."
#closes files open within target variable
target.close()