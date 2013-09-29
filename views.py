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
FACEBOOK_APP_SECRET = '	91e4d3b34430f67d65ad7ee76af65d28'


app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY
# oauth = OAuth()

# facebook = oauth.remote_app('facebook',
#     base_url='https://graph.facebook.com/',
#     request_token_url=None,
#     access_token_url='/oauth/access_token',
#     authorize_url='https://www.facebook.com/dialog/oauth',
#     consumer_key=FACEBOOK_APP_ID,
#     consumer_secret=FACEBOOK_APP_SECRET,
#     request_token_params={'scope': 'email'}
# )

# @facebook.tokengetter
# def get_facebook_token():
# 	return session.get('oauth_token')

@app.route('/')
def index():

    cookie = request.cookies.get("fbsr_" + FACEBOOK_APP_ID)
    friends = None
    if cookie:
        encoded_sig, payload = map(str, cookie.split('.', 1))
        sig = base64.urlsafe_b64decode(encoded_sig + "=" * ((4 - len(encoded_sig) % 4) % 4))
        data = base64.urlsafe_b64decode(payload + "=" * ((4 - len(payload) % 4) % 4))

        data = json.loads(data)
        user = facebook.get_access_token_from_code(data["code"], "", FACEBOOK_APP_ID, FACEBOOK_APP_SECRET)
    # user = facebook.get_user_from_cookie(request.cookies, FACEBOOK_APP_ID, FACEBOOK_APP_SECRET)
        if user:
            graph = facebook.GraphAPI(user["access_token"])
            profile = graph.get_object("me")
            friends = graph.get_connections("me", "friends")

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