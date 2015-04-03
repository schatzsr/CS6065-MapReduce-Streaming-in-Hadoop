#!/usr/bin/env python

import sys
import string

sums = 0
counts = 0
primes = 0
first = True

def isPrime(current):
    return all(current % i for i in xrange(2, current))

for line in sys.stdin:
    try:
        number = int(line.strip())
        sums += number
        counts += 1
        if isPrime(number):
            primes += 1
    except:
        continue

        
print 'Sum\t%s' % sums
print 'Count\t%s' % counts
print 'Prime\t%s' % primes
