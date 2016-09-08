read = open("ex19b.txt")
print "First line: %s" % read.read()

write = open("ex19b.txt", 'w')
read.write("apples")
print "Second line: %s" % write.read()
write.close()
read.close()

#reader = target.read()
#print reader


#def output(filename, body):
#filen = open('ex19b.txt', 'w')
#print filen
#filen.read()
#print filen
#filen.write("123456")
#filen.read()
#filen.close()

#print "What is the filename?"
#file_in = raw_input("> ")

#print "What is the body?"
#body_in = raw_input("> ")

#output("ex19b.txt", "asdf")