#!/usr/bin/python2.7
"""Task 3. HDFS with Python (Snakebite): createdir"""
import snakebite.client as sb


def createdir(l):
    """Creates the directories listed on l within HDFS."""
    client = sb.Client("hadoop3", 9000)
    for dir_name in client.mkdir(l, create_parent=True):
        print(dir_name)


if __name__ == "__main__":
    createdir(["/holbies/input"])
