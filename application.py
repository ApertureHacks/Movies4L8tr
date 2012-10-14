from flask import Flask
from flask import render_template
from flask import request
import urllib
from functions import *

app = Flask(__name__)

@app.route('/')
def home_page():
	mdict = get_upcoming(10);
	return render_template('main.html', mdict=mdict)

@app.route('/search', methods=['GET'])
def search_page():
	if '_title' in request.args:
		title = request.args['_title']
	else:
		title = "Batman"
	title = urllib.quote(title)
	print title
	mdict = search_movie(title)
	return render_template('main.html', mdict=mdict)

@app.route('/movie/<idnumber>')
def get_movie_by_id(idnumber):
	mdict = get_movie(idnumber)
	return render_template('movie.html', movie=mdict)

@app.route('/ajax/', methods=['POST'])
def answer_ajax():
	if 'name' in request.body:
		name = request.body['name']
	if 'email' in request.body:
		email = request.body['email']
	if 'phone' in request.body:
		phone = request.body['phone']
	if 'movie' in request.body:
		movie = request.body['movie']
	if 'release' in request.body:
		release = request.body['release']
	
	addto_db(name, movie, release, email, phone);

	return 'success'

if __name__ == '__main__':
	app.run(debug=True)
