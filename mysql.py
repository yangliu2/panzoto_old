#!/usr/bin/python
import MySQLdb

def create_table(tableName):
	
	db = MySQLdb.connect(host="localhost",    # your host, usually localhost
	                     user="root",         # your username
	                     passwd="Demo3456",  # your password
	                     db="panzoto")        # name of the data base

	# you must create a Cursor object. It will let
	#  you execute all the queries you need
	cur = db.cursor()

	# Use all the SQL you like
	cur.execute("SELECT * FROM " + tableName)

	# print all the first cell of all the rows
	for row in cur.fetchall():
	    print row[0]

	db.close()