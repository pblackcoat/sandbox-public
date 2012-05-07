import MySQLdb as mdb
import sys
import math

con = mdb.connect('wiki', 'blackcoat', 'password', 'test1')

with con:

        locationName = input('Please enter a Name for the location:')
        
        print #(locationName)
        print #("the %s is" % (locationName))
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS \
                Writers(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25))")
        #cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
        addLocation = cur.execute("INSERT INTO Writers(name) VALUES('%s')" % (locationName)) 

        cur.execute("SELECT * FROM Writers")
        data = cur.fetchall()

	
for row in data:
	print (data)
        
