#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """
    Access the database and retrieve the states
    that match the given name.
    """
    username = db.escape_string(argv[1])
    password = db.escape_string(argv[2])
    database = db.escape_string(argv[3])
    search_name = db.escape_string(argv[4])

    # Connect to the MySQL server
    db_connect = db.connect(host="localhost", port=3306,
                            user=username, passwd=password, db=database)
    db_cursor = db_connect.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
    db_cursor.execute(query, (search_name,))
    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
