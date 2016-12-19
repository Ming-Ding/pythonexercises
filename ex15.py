from sys import argv

script, user_name = argv
biubiu = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
loves = raw_input(biubiu)

print "Where are you from %s" % user_name
lives = raw_input(biubiu)

print "What's your favorite color?"
color = raw_input(biubiu)

print "Do you want to go home right now %s?" % user_name
feeling = raw_input(biubiu)

print """
Alright, so you said %r about liking me.
You come from %r. Thats a nice place.
Your favorite color is %r, I like it too.
%r, you can go home right now.
""" % (loves, lives, color, feeling)
