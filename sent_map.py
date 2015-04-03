#!/usr/bin/env python

import sys
import string

counter = 0
has_capital = True

for line in sys.stdin:
    for character in line:
        if character.isupper():
            counter = 1
            has_capital = True
        elif character in '.!?' and has_capital:
            counter += 1
            print 'SentenceCount\t%s' % counter
            has_capital = False
        else:
            counter +=1

# Use case to print the last fragment of a block, 
# if it satisfies the capital letter constraint.
if has_capital:
    print 'SentenceCount\t%s' % counter
