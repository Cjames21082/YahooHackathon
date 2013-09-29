import os
from flask import Flask, render_template, redirect
import urllib

app = Flask(__name__)

@app.route('/')
def hello():

	query = "SELECT location FROM page WHERE page_id IN\
			(SELECT page_id FROM location_post WHERE author_uid IN\
			(SELECT uid2 FROM friend WHERE uid1=me()))"

	print query

	query = urllib.quote(query)
	print(query) 

	url = "https://graph.facebook.com/fql?q=" + query
	data = urllib.urlopen(url).read()
	print(data)
	
 
	return render_template('index.html',
							data= data)



if __name__ == "__main__":
	app.run(debug = True)
