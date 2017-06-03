from flask import Response, current_app
import json


class ApplicationError(Exception):
    """

    This class is to be raised when the application identifies that there's been a problem
    and that the client should be informed.

    Example:
        raise ApplicationError("Title number invalid", "E102", 400)

    The handler method will then create the response body in a standard structure so clients
    will always know what to parse.

    """
    def __init__(self, message, code, http_code=500):
        Exception.__init__(self)
        self.message = message
        self.http_code = http_code
        self.code = code


def unhandled_exception(e):
    current_app.logger.exception('Unhandled Exception: %s', repr(e))
    return Response(response=json.dumps({"error_message": "Unexpected error.", "error_code": "XXX"}), status=500)


def application_error(e):
    return Response(response=json.dumps({"error_message": e.message, "error_code": e.code}), status=e.http_code)


def register_exception_handlers(app):
    app.register_error_handler(ApplicationError, application_error)
    app.register_error_handler(Exception, unhandled_exception)

    app.logger.info("Exception handlers registered")
