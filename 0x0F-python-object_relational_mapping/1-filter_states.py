#!/usr/bin/python3
"""select all states starting with 'N' from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY `id`")
    for i in cur.fetchall():
        if (i[1][0] == 'N'):
            print(i)
    cur.close()
    db.close()
