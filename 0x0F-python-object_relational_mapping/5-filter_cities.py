#!/usr/bin/python3
import sys
import MySQLdb


def select_states(username, password, dbname, search):
    '''select states by searched term'''
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=dbname,
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.name\
                FROM cities JOIN states ON cities.state_id=states.id\
                WHERE states.name=(%s)\
                ORDER BY cities.id ASC", (search, ))
    rows = cur.fetchall()
    print(', '.join([x[0] for x in rows]))
    cur.close()
    db.close()

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    name = sys.argv[3]
    search = sys.argv[4]
    select_states(user, passwd, name, search)
