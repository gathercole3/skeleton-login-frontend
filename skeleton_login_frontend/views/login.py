from flask import Blueprint, render_template, request, current_app, jsonify
import requests
import json

login = Blueprint('login', __name__)


@login.route("/login")
def display_login_page():
    return render_template('pages/display_logins.html')

@login.route("/login/oauthGoogleValidate", methods=['POST'])
def validate_google_token():
    post_data = request.form

    url = current_app.config["LOGIN_API_URL"] + "/verify_google_token"
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    payload = {}
    payload["token"] = post_data['authorization_grant']
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

    return response.text
