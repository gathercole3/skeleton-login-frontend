from skeleton_login_frontend import app
from skeleton_login_frontend.views import general

def register_blueprints(app):
    """
    Adds all blueprint objects into the app.
    """
    app.register_blueprint(general.general)

    # All done!
    app.logger.info("Blueprints registered")
