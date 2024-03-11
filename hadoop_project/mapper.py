#!/usr/bin/env python2
"""Task 6. MapReduce (mapper)"""
import csv
import sys

for row in csv.reader(sys.stdin):
    print(str(row[0]) + "\t" + str(row[1]) + "," + str(row[3]))
