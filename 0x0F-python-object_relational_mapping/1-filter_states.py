#!/usr/bin/python3
import sys
import MySQLdb


def select_states(username, password, dbname):
    '''select states with capital N'''
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=dbname,
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`\
                WHERE `name` REGEXP '^N' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        if ('N' in row[1]):
            print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    name = sys.argv[3]
    select_states(user, passwd, name)
