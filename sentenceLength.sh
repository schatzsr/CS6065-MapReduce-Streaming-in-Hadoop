#!/bin/bash
hadoop jar $HADOOP_INSTALL/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input $1 -output $2 -file sent_map.py sent_reduce.py -mapper sent_map.py -reducer sent_reduce.py
