from flask import Flask

app = Flask(__name__)

app.config.from_pyfile("config.py")

#these imports must be included after the app object has been created as it is imported in them
from skeleton-login-frontend.blueprints import register_blueprints

register_blueprints(app)
