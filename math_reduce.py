#!/usr/bin/env python

import sys
import string

sums = 0
counts = 0
primes = 0


for line in sys.stdin:
    (key,val) = line.strip().split('\t',1)
    try:
        number = int(val)
        if key == 'Sum':
            sums += number
        elif key == 'Count':
            counts += number
        elif key == 'Prime':
            primes += number
    except:
        continue
        
print 'Sum\t%s' % sums
print 'Count\t%s' % counts
print 'Prime\t%s' % primes
