from werkzeug.exceptions import HTTPException


def error_handler(app):
    @app.errorhandler(HTTPException)
    def handle_bad_request(e):
        return e.description, e.code


