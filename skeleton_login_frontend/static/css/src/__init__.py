from flask import Flask
from flask_oauthlib.client import OAuth

app = Flask(__name__)


SECRET_KEY = 'development key'
DEBUG = True


app.debug = DEBUG
app.secret_key = SECRET_KEY
oauth = OAuth()

app.config['GOOGLE_ID'] = "480105099153-8tdge3cp2v4d5g550tjsov24p9tdlb9v.apps.googleusercontent.com"
app.config['GOOGLE_SECRET'] = "BYvvDIDMaAVh2wxgMX1mo9Ci"
app.config['FACEBOOK_APP_ID'] = '170777273409829'
app.config['FACEBOOK_APP_SECRET'] = 'd412cc0114170fe5c9783b9de7540015'
app.debug = True


facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=app.config.get('FACEBOOK_APP_ID'),
    consumer_secret=app.config.get('FACEBOOK_APP_SECRET'),
    request_token_params={'scope': 'email'}
)

google = oauth.remote_app(
    'google',
    consumer_key=app.config.get('GOOGLE_ID'),
    consumer_secret=app.config.get('GOOGLE_SECRET'),
    request_token_params={
        'scope': 'email'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

from src import views
