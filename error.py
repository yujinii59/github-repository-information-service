from werkzeug.exceptions import HTTPException
from exception.custom_exception import TokenException


def error_handler(app):
    @app.errorhandler(HTTPException)
    def handle_bad_request(e):
        return 'error!!!!!!!!!', e.code

    @app.errorhandler(TokenException)
    def handle_token_error(e):
        return e.dev_error_message, e.status_code

