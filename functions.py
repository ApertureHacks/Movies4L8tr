import json
import urllib2
import urllib
import sendgrid
import MySQLdb
import MySQLdb.cursors
from twilio.rest import TwilioRestClient
from config import *
from pprint import *

db = MySQLdb.connect(host='localhost', user='root', passwd=dbpass, db='movie_users')

def get_upcoming(n):
	url = 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies/upcoming.json?apikey='+rt_key+'&page_limit='+str(n)
	u = urllib2.urlopen(url)
	result = json.load(u);
	u.close()
	movies = result['movies']
	#for movie in movies:
	#	r['m' + str(i)] = {'title': movie['title'], 'release-dates': movie['release_dates']['theater'], 'poster': movie['posters']['detailed']}
	return movies

def search_movie(name):
	#name = urllib.urlencode(name)
	url = 'http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey='+rt_key+'&q='+name+'&page_limit=5'
	u = urllib2.urlopen(url)
	result = json.load(u);
	u.close()
	movies = result['movies']
	#for movie in movies:
	#	r[i] = {'title': movie['title'], 'release-dates': movie['release_dates']['theater'], 'poster': movie['posters']['detailed']}
	#	i=i+1
	return movies

def get_movie(index):
	url = 'http://api.rottentomatoes.com/api/public/v1.0/movies/'+index+'.json?apikey='+rt_key
	u = urllib2.urlopen(url)
	result = json.load(u);
	u.close()
	return result

def addto_db(user, movie, release, email, phone):
	#db = MySQLdb.connect(host='localhost', user='root', passwd=dbpass, db='movie_users', cursorclass='MySQLdb.cursors.DictCursor')
	#import pdb; pdb.set_trace()
	cursor = db.cursor()
	try:
		cursor.execute("""INSERT INTO users(name, movietitle, releasedate, email, phone) VALUES ("%s","%s",%s,"%s","%s")""",(user,movie,release,email,phone))
		db.commit()
		return True
	except:
		db.rollback()
		return False

def get_old():
	#db = MySQLdb.connect(host='localhost', user='root', passwd=dbpass, db='movie_users', cursorclass='MySQLdb.cursors.DictCursor')
	db = MySQLdb.connect(host='localhost', user='root', passwd=dbpass, db='movie_users')
	#import pdb; pdb.set_trace()
	cursor = db.cursor()
	cursor.execute("SELECT * FROM users")
	rows = cursor.fetchall()
	for row in rows:
		data = {}
		data['name'] = row[1][1:][:-1]
		data['title'] = row[2][1:][:-1]
		data['email'] = row[4][1:][:-1]
		data['phone'] = row[5][1:]
		send_text(data['name'], data['title'], data['phone'])
		send_email(data['name'], data['title'], data['email'])
	cursor.execute("TRUNCATE TABLE users")

def send_text(user, movie, phone):
	phone = "+1"+phone
	print phone
	account = tw_account
	token = tw_token
	sender = tw_sender
	client = TwilioRestClient(account, token)
	text = 'Hello '+user+'! The movie '+movie+' has been released today! Go see it in a theater near you!'
	message = client.sms.messages.create(to=unicode(phone), from_=sender, body=text)
	return

def send_email(user, movie, email):
	print user
	print movie
	print email
	s = sendgrid.Sendgrid(sg_user, sg_pass, secure=True)
	message = sendgrid.Message(sg_email, movie+' Has Been Released', 'Hello '+user+'! The movie '+movie+' has been released today. Go see it in a theater near you!')
	message.add_to(email, user)
	s.smtp.send(message)
