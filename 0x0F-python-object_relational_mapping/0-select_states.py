#!/usr/bin/python3
"""
     That Script lists all states from the database 'hbtn_0e_0_usa'.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # For Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # For Create cursor object
    cursor = db.cursor()

    # For Execute the query to select all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # For Fetch all the rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # For Close the cursor and database connection
    cursor.close()
    db.close()
