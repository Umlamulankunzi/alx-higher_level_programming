#!/usr/bin/python3
"""Takes in the name of a state as an argument and lists
All cities of that state, using the database hbtn_0e_4_usa"""
import sys
import MySQLdb


# DATABASE CONFIG VARIABLES
HOST = "localhost"
USR = sys.argv[1]
PASSWD = sys.argv[2]
DB = sys.argv[3]
PORT = 3306
QUERY = """SELECT cities.name FROM
            cities INNER JOIN states ON states.id=cities.state_id
            WHERE states.name=%s"""


if __name__ == "__main__":
    db = MySQLdb.connect(host=HOST, user=USR, passwd=PASSWD, db=DB, port=PORT)
    cur = db.cursor()
    cur.execute(QUERY, (sys.argv[4],))
    rows = cur.fetchall()
    results = [row[0] for row in rows]
    print(*results, sep=", ")
    cur.close()
    db.close()
