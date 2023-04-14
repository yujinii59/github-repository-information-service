from werkzeug.exceptions import InternalServerError, NotFound
from exception.custom_exception import TokenException, NotExistException


def error_handler(app):
    # access with wrong url
    @app.errorhandler(NotFound)
    def handle_not_found(e):
        return 'This url format is wrong. Insert the url formated : <127.0.0.1:5000/<naming list seperated by comma>', e.code

    # internal error
    @app.errorhandler(InternalServerError)
    def handle_sever_error(e):
        return e.description, e.code

    # the access token is wrong or not found
    @app.errorhandler(TokenException)
    def handle_token_error(e):
        return e.dev_error_message, e.status_code

    # some repository's name in endpoints doesn't exist
    @app.errorhandler(NotExistException)
    def handle_token_error(e):
        return e.dev_error_message, e.status_code
