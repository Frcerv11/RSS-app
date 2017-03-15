import sqlite3 as lite
import sys

con = lite.connect('rss_app.db')
#Check if username and password exists in the database   
def processCredentials(user,pswd):
	global y
	cur = con.cursor() 
	cur.execute('SELECT * FROM User WHERE Username="%s" AND Password="%s"' % (user, pswd))
	if cur.fetchone():
	    return True
	else:
	   	return False

def getFeedUrls(user,pswd):
	con.row_factory = lambda cursor, row: row[1]
	c = con.cursor()
	ids = c.execute('SELECT f.userId, f.url FROM feeds f WHERE f.userId IN(SELECT id FROM user WHERE id = f.userId AND Username="%s" AND Password="%s")' % (user, pswd)).fetchall()
	return ids

def storeUrl(url):
	print(url)