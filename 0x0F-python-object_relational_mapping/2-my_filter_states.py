#!/usr/bin/python3
"""Takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument."""
import sys
import MySQLdb


# DATABASE CONFIG VARIABLES
HOST = "localhost"
USR = sys.argv[1]
PASSWD = sys.argv[2]
DB = sys.argv[3]
PORT = 3306
QUERY = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(sys.argv[4])


if __name__ == "__main__":
    db = MySQLdb.connect(host=HOST, user=USR, passwd=PASSWD, db=DB, port=PORT)
    cur = db.cursor()
    cur.execute(QUERY)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
