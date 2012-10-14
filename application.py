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

@app.route('/ajax', methods=['POST'])
def answer_ajax():
	print "ajax call reveived"
	if 'name' in request.form:
		name = request.form['name']
	if 'email' in request.form:
		email = request.form['email']
	else:
		email = "nope"
	if 'phone' in request.form:
		phone = request.form['phone']
	else:
		phone = "nope"
	if 'movie' in request.form:
		movie = request.form['movie']
	if 'release' in request.form:
		release = request.form['release']
	
	addto_db(name, movie, release, email, phone);

	return 'success'

if __name__ == '__main__':
	app.run(debug=True)
