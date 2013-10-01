from flask import Flask, redirect, url_for, session, request, render_template
# from flask_oauth import OAuth
import facebook
import base64
import urllib
import urllib2
import json


SECRET_KEY = 'development key'
DEBUG = True
FACEBOOK_APP_ID = '657737804244482'
FACEBOOK_APP_SECRET = '152696f9db120ef7d0bf878e7f73a5b0'


app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY

@app.route('/')
def index():

   

if __name__ == '__main__':
    app.run()