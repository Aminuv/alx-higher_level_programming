#!/usr/bin/python3
"""
   To Displays all values in the states table of the database hbtn_0e_0_usa
whose name matches that supplied as argument.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           password=sys.argv[2], db=sys.argv[3], port=3306,
                           charset="utf8")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'".format(
                                                            sys.argv[4]))
    query = cursor.fetchall()
    for states in query:
        print(states)
    cursor.close()
    conn.close()
