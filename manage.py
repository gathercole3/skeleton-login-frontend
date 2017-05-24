from flask_script import Manager
from skeleton_login_frontend import app
import os

manager = Manager(app)

@manager.command
def runserver(port=9998):
    """Run the app using flask server"""

    os.environ["PYTHONUNBUFFERED"] = "yes"
    os.environ["LOG_LEVEL"] = "DEBUG"
    os.environ["COMMIT"] = "LOCAL"

    app.run(debug=True, port=int(port))

if __name__ == "__main__":
    manager.run()
