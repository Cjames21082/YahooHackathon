from flask import Flask, redirect, url_for, session, request, render_template
from flask_oauth import OAuth
import facebook


SECRET_KEY = 'development key'
DEBUG = True
FACEBOOK_APP_ID = '657737804244482'
FACEBOOK_APP_SECRET = '	91e4d3b34430f67d65ad7ee76af65d28'


app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY
oauth = OAuth()

fb = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=FACEBOOK_APP_ID,
    consumer_secret=FACEBOOK_APP_SECRET,
    request_token_params={'scope': 'email'}
)

# @facebook.tokengetter
# def get_facebook_token():
# 	return session.get('oauth_token')

@app.route('/')
def index():

    access_token = facebook.get_app_access_token(FACEBOOK_APP_ID, FACEBOOK_APP_SECRET)
    graph = facebook.GraphAPI(access_token)
    user = graph.get_object("me")
    friends = graph.get_connections(user["id"], "friends")
    

    return render_template('index.html',
                            friends= friends)


# @app.route('/login')
# def login():
#     return fb.authorize(callback=url_for('facebook_authorized',
#         next=request.args.get('index') or request.referrer or None,
#         _external=True))
#     # redirect("https://www.facebook.com/dialog/oauth?client_id=%s&redirect_url)


# @app.route('/login/authorized')
# @facebook.authorized_handler
# def facebook_authorized(resp):
#     if resp is None:
#         return 'Access denied: reason=%s error=%s' % (
#             request.args['error_reason'],
#             request.args['error_description']
#         )
#     session['oauth_token'] = (resp['access_token'], '')
#     me = facebook.get('/me')
#     return 'Logged in as id=%s name=%s redirect=%s' % \
#         (me.data['id'], me.data['name'], request.args.get('next'))


if __name__ == '__main__':
    app.run()