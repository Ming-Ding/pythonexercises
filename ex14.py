from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first favorite fruit is:", first
print "your second favorite fruit is:", second
print "Your third favorite fruit is:", third


print "What was the first favorite fruit?",
first = raw_input()
print "what was the second favorite fruit?",
second = raw_input()
print "what was the third favorite fruit?",
third = raw_input()

print "so, your favorite fruits are %r, %r, %r." % (
    first, second, third)
