# this one is like your scripts with argv
def go_nuts(*args):
    arg1, arg2 = args
    print "bingo: %r, blabla: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def go_nuts_again(arg1, arg2):
    print "biubiu: %r, gogogo: %r" % (arg1, arg2)

# this just takes one argument
def go_chiao(arg1):
    print "chiao: %r" % arg1

# this one takes no arguments
def chiao_this():
    print "I got everything'."


go_nuts("Zed","Shaw")
go_nuts_again("Zed","Shaw")
go_chiao("First!")
chiao_this()
