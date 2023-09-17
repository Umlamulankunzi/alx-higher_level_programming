#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import sys
import MySQLdb


if __name__ == "__main__":
    # DATABASE CONFIG VARIABLES
    HOST = "localhost"
    USR = sys.argv[1]
    PASSWD = sys.argv[2]
    DB = sys.argv[3]
    PORT = 3306
    QUERY = """SELECT * FROM states
                WHERE name LIKE BINARY 'N%'
                ORDER BY states.id"""

    db = MySQLdb.connect(host=HOST, user=USR, passwd=PASSWD, db=DB, port=PORT)
    cur = db.cursor()
    cur.execute(QUERY)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
