import MySQLdb as mdb
import sys
import math

con = mdb.connect('wiki', 'blackcoat', 'password', 'test2')

with con:

        cur = con.cursor()
        cur.execute("SELECT * FROM location")

        data = cur.fetchall()

        for row in data:
                print (data)
