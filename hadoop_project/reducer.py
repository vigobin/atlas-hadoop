#!/usr/bin/env python2
"""Task 7. MapReduce (reducer)"""
import sys

top_salaries = []

for line in sys.stdin:
    try:
        id, company_total = line.strip().split("\t")
        company, totalyearlycompensation = company_total.split(",")
        totalyearlycompensation = float(totalyearlycompensation)

        top_salaries.append((id, totalyearlycompensation, company))

        # Keep only the top 10 salaries
        top_salaries.sort(key=lambda x: x[1], reverse=True)
        top_salaries = top_salaries[:10]
    except ValueError:
        # Skip rows with incorrect format
        pass

print("id\tSalary\tcompany")

for id, salary, company in top_salaries:
    print("{}\t{}\t{}".format(id, salary, company))
