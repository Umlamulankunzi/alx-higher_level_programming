#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""
import sys
import MySQLdb


# DATABASE CONFIG VARIABLES
HOST = "localhost"
USR = sys.argv[1]
PASSWD = sys.argv[2]
DB = sys.argv[3]
PORT = 3306
QUERY = """SELECT cities.id, cities.name, states.name
            FROM cities INNER JOIN states ON states.id=cities.state_id"""


if __name__ == "__main__":
    db = MySQLdb.connect(host=HOST, user=USR, passwd=PASSWD, db=DB, port=PORT)
    cur = db.cursor()
    cur.execute(QUERY)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
