import sqlite3 as lite
import sys

con = lite.connect('rss_app.db')

#Check if username and password exists in the database   
def processCredentials(user,pswd):
	cur = con.cursor() 
	cur.execute('SELECT * from User WHERE Username="%s" AND Password="%s"' % (user, pswd))
	if cur.fetchone():
	    return True
	else:
	   	return False
