import json
import urllib2
import urllib
from config import *

def get_upcoming(n):
	r = {}
	url = 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies/upcoming.json?apikey='+rt_key+'&page_limit='+str(n)
	u = urllib2.urlopen(url)
	result = json.load(u);
	u.close()
	movies = result['movies']
	i=1
	for movie in movies:
		r[i] = {'title': movie['title'], 'release-dates': movie['release_dates']['theater'], 'poster': movie['posters']['detailed']}
		i=i+1
	return r

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
