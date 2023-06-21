#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """
    Connect to the MySQL server and retrieve all cities.
    """
    username = db.escape_string(argv[1])
    password = db.escape_string(argv[2])
    database = db.escape_string(argv[3])

    # Connect to the MySQL server
    db_connect = db.connect(host="localhost", port=3306,
                            user=username, passwd=password, db=database)
    db_cursor = db_connect.cursor()

    query = "SELECT * FROM cities ORDER BY cities.id ASC"
    db_cursor.execute(query)
    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
