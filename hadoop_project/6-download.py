#!/usr/bin/python2.7
"""Task 5. HDFS with Python (Snakebite): download"""
import snakebite.client as sb


def download(l):
    """Retrieves from the HDFS files listed in l and store them in the
        home /tmp folder of the user."""
    client = sb.Client("localhost", 9000)

    for hdfs_file in client.copyToLocal(l, '/tmp'):
        print(hdfs_file)
