from skeleton_login_frontend import app
from skeleton_login_frontend.views import general, login

def register_blueprints(app):
    """
    Adds all blueprint objects into the app.
    """
    app.register_blueprint(general.general)
    app.register_blueprint(login.login)

    # All done!
    app.logger.info("Blueprints registered")
