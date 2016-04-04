import sys

def hashbang(start, end):
    for i in xrange(start, end):
        #newline is added for some prettiness
        newline = False
        if i % 3 == 0:
            print "hash",
            newline = True
        if i % 5 == 0:
            print "bang",
            newline = True
        if newline:
            print ""

if __name__ == '__main__':

    first = int(sys.argv[1])
    last  = int(sys.argv[2])

    hashbang(first, last)
