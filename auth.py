import sqlite3 as lite
import sys

con = lite.connect('rss_app.db')
#Check if username and password exists in the database   
def processCredentials(user,pswd):
	cur = con.cursor() 
	cur.execute('SELECT * FROM User WHERE Username="%s" AND Password="%s"' % (user, pswd))
	if cur.fetchone():
	    return True
	else:
	   	return False

def getUserId(user,pswd):
	con.row_factory = lambda cursor, row: row[0]
	c = con.cursor()
	row = c.execute('SELECT Id FROM User WHERE Username="%s" AND Password="%s"' % (user, pswd)).fetchall()
	return row[0]
	# return userID
def getFeedUrls(user,pswd):
	con.row_factory = lambda cursor, row: row[1]
	c = con.cursor()
	ids = c.execute('SELECT f.userId, f.url FROM feeds f WHERE f.userId IN(SELECT id FROM user WHERE id = f.userId AND Username="%s" AND Password="%s")' % (user, pswd)).fetchall()
	return ids

def saveEntry(username,password,url):
	userId = getUserId(username,password)
	with con:
		cur = con.cursor()    
		cur.execute("INSERT INTO Feeds (UserId,URL) VALUES ( ?, ?)",(userId, url))
	return True

def deleteEntry(username,password,url):
	userId = getUserId(username,password)
	print(url,int(userId))
	cur = con.cursor()    
	cur.execute("DELETE FROM Feeds WHERE URL=? AND UserId IN (SELECT id FROM user WHERE id = ?)", (url,int(userId)))	
	con.commit()
	return True;

def userExist(username):
	cur = con.cursor() 
	cur.execute('SELECT 1 from User where Username = "%s"' % (username))
	if cur.fetchone():
	    return True
	else:
	   	return False
	
def saveUser(username,password):
	if(userExist(username) == False):
		with con:
			cur = con.cursor()    
			cur.execute("INSERT INTO User (Username,Password) VALUES ( ?, ?)",(username, password))
		return True
	else:
		return False

def sortByName(user,pswd):
	con.row_factory = lambda cursor, row: row[1]
	c = con.cursor()
	ids = c.execute('SELECT f.userId, f.url FROM feeds f WHERE f.userId IN(SELECT id FROM user WHERE id = f.userId AND Username="%s" AND Password="%s")' % (user, pswd)).fetchall()
	return ids
# con = lite.connect('rss_app.db')
# cur = con.cursor()  
# c.executemany('INSERT INTO Feeds(UserId, URL) VALUES (?,?)', data_person_name)

