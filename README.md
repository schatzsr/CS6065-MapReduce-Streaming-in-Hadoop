MapReduce Streaming in Hadoop
================

CS6065 Intro to Cloud Computing Homework 4

*Cloned from University of Cincinnati's git site, https://github.uc.edu/*

*Assignment Outline: https://docs.google.com/document/d/1MM6fuwN84iHzwZJ92D6z13jnVvwnAtnqoFEduTaNH6A/*

#### Example Output
```
mathstats.sh:
>> ./mathstats.sh /data/numbers/small.txt output
...
>> hadoop fs -cat /user/<username>/output/part-00000
Count  	10
Sum  		70909325
Prime  	0

>> ./mathstats.sh /data/numbers/medium.txt output2
...
>> hadoop fs -cat /user/<username>/output2/part-00000
Count  	1234567
Sum  		6172269075
Prime  	312437

>> ./mathstats.sh /data/numbers output3
...
>> hadoop fs -cat /user/<username>/output3/part-00000
Count  	40224475
Sum  		194921459755704
Prime  	5767703


sentenceLength.sh:
>> ./sentenceLength.sh /data/books/TSEliiot.txt eliot
...
>>hadoop fs -cat /user/<username>/eliot
SentenceCount	507
AvgSentenceLength	35.433

>> ./sentenceLength.sh /data/books/TheCountofMonteCristo.txt thecount
...
>>hadoop fs -cat /user/<username>/thecount
SentenceCount	27039
AvgSentenceLength	56.779

>> ./sentenceLength.sh /data/books allbooks
...
>>hadoop fs -cat /user/<username>/allbooks
SentenceCount	473153
AvgSentenceLength	49.257
```