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
	title = request.args['_title']
	title = urllib.quote(title)
	print title
	mdict = search_movie(title)
	return render_template('main.html', mdict=mdict)

@app.route('/movie/<idnumber>')
def get_movie_by_id(idnumber):
	mdict = get_movie(idnumber)
	return render_template('movie.html', movie=mdict)

if __name__ == '__main__':
	app.run(debug=True)
