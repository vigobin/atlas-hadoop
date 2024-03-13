#!/usr/bin/env python2
"""Task 7. MapReduce (reducer)"""
import sys

top_salaries = []

for line in sys.stdin:
    try:
        id_, company_total = line.strip().split("\t")
        company, totalyearlycompensation = company_total.split(",")
        totalyearlycompensation = float(totalyearlycompensation)

        top_salaries.append((company, totalyearlycompensation))

        # Keep only the top 10 salaries
        top_salaries.sort(key=lambda x: x[1], reverse=True)
        top_salaries = top_salaries[:10]
    except ValueError:
        # Skip rows with incorrect format
        pass

for company, salary in top_salaries:
    print(company + "\t" + "{:.2f}".format(salary))
