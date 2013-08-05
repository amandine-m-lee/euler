import math, heapq

"""brainstorming:
    work backwards
    dynamic programming
    checking for primes is easier upwards
    it can't handle a seive of 900 million
    however, it can handle a seive of sqrt(900 million)"""
LIMIT = 31427 
SIEVE = []
NUMS = list('123456789')
PPS = set()


def gen_sieve():
   
    options = set(xrange(2,LIMIT))

    curr = options.pop()
    while len(options) > 0:
        for i in xrange(1, LIMIT/curr):
            mult = i * curr
            if mult in options:
                options.remove(mult)
        heapq.heappush(SIEVE, curr)
        curr = options.pop()

def is_prime(num):
    primes = list(SIEVE) 
    curr = heapq.heappop(primes)
    while curr < math.sqrt(num):
        if num % curr == 0:
            return False
        curr = heapq.heappop(primes)
    return True
        
def is_pandigital(num):
    elements = list(str(num))
    elements.sort()
    return elements == NUMS[0:len(elements)]

    
if __name__ == '__main__':
    gen_sieve()
    for poss in xrange(2, 7654321):
        if is_pandigital(poss):
            print poss
            if is_prime(poss):
                PPS.add(poss)
    print len(PPS)
                
        







"""NUMS = '123456789'
BIGGEST = 1

stream = xrange(987654321, 0, -1)

yatta = False
i = 0

import itertools as it

longest-combos = [int(''.join(list(item))) for item in it.permutations(NUMS)]

while not yatta:
    if isPrime("""




"""def isPrime(n):
    for prime in PRIMES:
        if prime > math.sqrt(n):
            PRIMES.append(n)
            return True

        elif n % prime == 0:
            return False
    else:
        PRIMES.append(n)
        return True

if __name__ == '__main__':


    for n in xrange(3, 987654322):
        s = str(n)
        length = len(s)
        must = set(NUMS[0:length])
        if isPrime(n):
            for digit in s:
                if digit in must:
                    must.remove(digit)
                else:
                    break
            else:
                BIGGEST = n
                print n

    print "BIGGEST:", n"""

#Sieve impelementation backwards. 


"""def isPandigital(n):
    s = str(n)
    length = len(s)
    must = set(NUMS[0:length])
    
    for digit in s:
        if digit in must:
            must.remove(digit)
        else:
            return False
    else:
        return True
if __name__ == '__main__':
    

#Go backwards?
    while len(POSS) > 0:
        n = POSS.pop()
        print n
        for i in xrange(1, (987654322/n)):
            m = n * i 
            if m in POSS:
                print POSS.remove(m)
        if isPandigital(n):
            print n
            BIGGEST = n"""
            
        

