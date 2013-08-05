PI = {}
BESTLEN = 0
BESTVAL = 0


def next_collatz(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n + 1

def collatz_length(num):

    if num == 1:
        return 0

    if not num in PI:
        PI[num] = 1 + collatz_length(next_collatz(num))

    return PI[num]



for i in xrange(1, 1000000):
    l = collatz_length(i)
    if l > BESTLEN:
        BESTLEN = l
        BESTVAL = i

print "BESTT::::", BESTVAL, BESTLEN


    

