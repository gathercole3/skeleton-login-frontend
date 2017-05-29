from flask import Blueprint, render_template, request

login = Blueprint('login', __name__)


@login.route("/login")
def display_login_page():
    return render_template('pages/display_logins.html')

@login.route("/login/oauthGoogleValidate", methods=['POST'])
def validate_google_token():
    post_data = request.form
    return post_data['authorization_grant']
