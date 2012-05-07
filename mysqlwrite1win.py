import MySQLdb as mdb
import sys
import math

con = mdb.connect('wiki', 'blackcoat', 'password', 'test1')

with con:

        #locationName = input('Please enter a Name for the location:')
        
        #print (locationName)
        #print ("the %s is" % (locationName))
        cur = con.cursor()
        buildDB = cur.execute("CREATE TABLE IF NOT EXISTS \
			Locationv2(uuid INT PRIMARY KEY AUTO_INCREMENT,\
			Name VARCHAR(50),\
			xcord INT,\
			ycord INT,\
			buildingType TINYINT UNSIGNED)")
#			INDEX `uuid` (`uuid`)
        #cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
        #addLocation = cur.execute("INSERT INTO Writers(name) VALUES('%s')" % (locationName)) 

        cur.execute("DESCRIBE Locationv2")
        data = cur.fetchall()

	
for row in data:
	print (data)
        
