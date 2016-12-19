
from sys import argv

script, a = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

cf = open(a)

print "First Let's print the whole file:\n"

print_all(cf)

print "Now let's rewind, kind of like a tape."

rewind(cf)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, cf)

current_line += 1

print_a_line(current_line, cf)

current_line += 1
print_a_line(current_line, cf)
