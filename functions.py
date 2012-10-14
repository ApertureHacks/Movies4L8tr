import json
import urllib2
import urllib
import _mysql
import sendgrid
from twilio.rest import TwilioRestClient
from config import *

def get_upcoming(n):
	r = {}
	url = 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies/upcoming.json?apikey='+rt_key+'&page_limit='+str(n)
	u = urllib2.urlopen(url)
	result = json.load(u);
	u.close()
	movies = result['movies']
	#for movie in movies:
	#	r['m' + str(i)] = {'title': movie['title'], 'release-dates': movie['release_dates']['theater'], 'poster': movie['posters']['detailed']}
	return movies

def get_movie(name):
	r = {}
	#name = urllib.urlencode(name)
	url = 'http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey='+rt_key+'&q='+name+'&page_limit=5'
	u = urllib2.urlopen(url)
	result = json.load(u);
	u.close()
	movies = result['movies']
	i=1
	for movie in movies:
		r[i] = {'title': movie['title'], 'release-dates': movie['release_dates']['theater'], 'poster': movie['posters']['detailed']}
		i=i+1
	return r

def addto_db(user, movie, release, email, phone):
	db = _mysql.connect(host='localhost', user='root', passwd=dbpass, db='movie_users')
	cursor = db.cursor()
	try:
		cursor.execute("""INSERT INTO users VALUES (%s,%s,%s,%s,%s)""",(user,movie,release,email,phone)
		db.commit()
		return True
	except:
		db.rollback()
		return False

def send_text(user, movie, phone):
	account = tw_account
	token = tw_token
	sender = tw_sender
	client = TwilioRestClient(account, token)
	text = 'Hello '+user+'! The movie '+movie+' has been released today! Go see it in a theater near you!'
	message = client.sms.messages.create(to='+1'+phone, from=sender, body=text)
	return

def send_email(user, movie, email):
	s = sendgrid.Sendgrid(sg_user, sg_pass, secure=True)
	message = sendgrid.Message(sg_email, movie+' Has Been Released', 'Hello '+user+!' The movie '+movie+' has been released today. Go see it in a theater near you!')
	message.add_to(email, user)
	s.smtp.send(message)
