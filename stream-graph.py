#!/usr/bin/env python

"""
stream-graph.py

Stream has two types of lines that are interesting for a graph:

Number of Threads requested = 1
Triad:       4230.1227       0.7604       0.7593       0.7617
Number of Threads requested = 2
Triad:       8923.7072       0.3604       0.3599       0.3608

Parse a file that contains those and produce something suitable
for input to gnuplot:

1 4230.1227
2 8923.7072
"""

import sys, string

current_threads=None

print "# threads,triad MB/s"
lines = sys.stdin.readlines()
for line in lines: 
    line=line.rstrip()
    pos=line.find("Number of Threads requested = ")
    if (pos==0):
        (junk,threads)=line.split("=",1)
        threads=threads.strip()
        if (threads.isdigit()):
            try:
                current_threads=int(threads)
            except:
                print "Confused by this line:"
                print line
    else:
        pos=line.find("Triad:")
        if (pos==0):
            try:
                (junk,triad,avg,min,max)=line.split()
                print current_threads,triad
            except:
                print "Confused by this line:"
                print line
