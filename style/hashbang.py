import sys

def hashbang(start, end):
    for i in xrange(start, end):
        if i % 3 == 0:
            print "hash"
        if i % 5 == 0:
            print "bang"

if __name__ == '__main__':

    first = int(sys.argv[1])
    last  = int(sys.argv[2])

    hashbang(first, last)
