from flask import Flask

app = Flask(__name__)

app.config.from_pyfile("config.py")

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

#these imports must be included after the app object has been created as it is imported in them
from skeleton_login_frontend.blueprints import register_blueprints
from skeleton_login_frontend.exceptions import register_exception_handlers

register_exception_handlers(app)
register_blueprints(app)
