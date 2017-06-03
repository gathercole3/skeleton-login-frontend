from flask import Blueprint, render_template, request, current_app, jsonify, session
import requests
import json
from skeleton_login_frontend.exceptions import ApplicationError

login = Blueprint('login', __name__)


@login.route("/login")
def display_login_page():
    return render_template('pages/display_logins.html')

@login.route("/login/oauth")
def display_oauth_login_page():
    return render_template('pages/display_oauth_logins.html')

@login.route("/login/oauthGoogleValidate", methods=['POST'])
def validate_google_token():
    post_data = request.form

    url = current_app.config["LOGIN_API_URL"] + "/verify_google_token"
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    payload = {}
    payload["token"] = post_data['authorization_grant']
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    json_data = json.loads(response.text)

    session['user-id'] = json_data['id']
    session['google_login'] = True

    return response.text

@login.route("/login/validate_login", methods=['POST'])
def validate_login():
    post_data = request.form

    url = current_app.config["LOGIN_API_URL"] + "/verify_login"
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    payload = {}
    payload["email"] = post_data['email']
    payload["password"] = post_data['password']
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

    json_data = json.loads(response.text)

    if response.status_code != 200:

        #code u001 has been specified to be an incorrect email and password combination so we should check for this
        if json_data['error_code'] == 'u001':
            return "incorrect email and password combo"

        raise ApplicationError("something has gone wrong trying to log you in", 'unspecified')
    session['user-id'] = json_data['id']
    session['google_login'] = True

    return response.text

@login.route("/logout")
def display_logout_page():
    session.clear()
    return render_template('pages/display_logout.html', googleLogin=googleLogin)
