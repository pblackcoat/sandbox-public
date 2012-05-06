#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

con = mdb.connect('localhost', 'root', '', 'test2')

with con:

	cur = con.cursor()
	cur.execute("SELECT * FROM location")

	data = cur.fetchall()
	
	for row in data:
		print data
