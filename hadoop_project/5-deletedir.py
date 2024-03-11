#!/usr/bin/python2.7
"""Task 4. HDFS with Python (Snakebite): deletedir"""
import snakebite.client as sb


def deletedir(l):
    """Removes the directories listed on l within HDFS."""
    client = sb.Client("localhost", 9000)
    try:
        for dir_name in client.delete(l, recurse=True):
            print(dir_name)
    except Exception:
        pass


if __name__ == "__main__":
    deletedir(["/holbies/input"])
