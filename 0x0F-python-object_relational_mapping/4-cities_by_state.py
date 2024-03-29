#!/usr/bin/python3
"""
    To Lists of all cities to the database 'hbtn_0e_4_usa',
    ordered by 'city id'.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           password=sys.argv[2], db=sys.argv[3], port=3306,
                           charset="utf8")
    cursor = conn.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM
                   cities INNER JOIN states ON states.id=cities.state_id""")
    query = cursor.fetchall()
    for states in query:
        print(states)
    cursor.close()
    conn.close()
