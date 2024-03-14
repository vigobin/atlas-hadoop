#!/usr/bin/env python2
"""Task 6. MapReduce (mapper) in a Hadoop environment.
    Takes the rows of the salaries.csv and prints the id,
        the company and the totalyearlycompensation items."""
import csv
import sys

for row in csv.reader(sys.stdin, delimiter=','):
    print('{}\t{},{}'.format(row[0], row[1], row[3]))
