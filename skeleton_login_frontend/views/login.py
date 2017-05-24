from flask import request, Blueprint, Response, jsonify, current_app

login = Blueprint('login', __name__)


@login.route("/login")
def display_login_page():
    return "tmp"
