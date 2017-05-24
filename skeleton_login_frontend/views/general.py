from flask import request, Blueprint, Response, jsonify, current_app

general = Blueprint('general', __name__)


@general.route("/health")
def check_status():
    return jsonify({
        "app": current_app.config["APP_NAME"],
        "status": "OK",
        "headers": request.headers.to_list(),
    })

@general.route("/showcase")
def showcase_temp():
    return "this is a test route for the plymouth university showcase"
