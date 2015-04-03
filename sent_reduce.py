#!/usr/bin/env python

import sys
import string


sent_count = 0
sent_sum = 0

for line in sys.stdin:
    (key,val) = line.strip().split('\t',1)
    try:
        number = int(val)
        if key == 'SentenceCount':
            sent_count += 1
            sent_sum += number
            

    except:
        continue
        
print 'SentenceCount\t%s' % sent_count
print 'AvgSentenceLength\t%s' % round((float(sent_sum)/float(sent_count)), 3)
