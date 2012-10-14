from flask import Flask
from flask import render_template
from functions import *
app = Flask(__name__)

@app.route('/')
def home_page():
	mdict = get_upcoming(10);
	return render_template('main.html', mdict=mdict)

if __name__ == '__main__':
	app.run()
