from flask import Blueprint, render_template

login = Blueprint('login', __name__, template_folder='templates')


@login.route("/login")
def display_login_page():
    return render_template('pages/display_logins.html')
