from werkzeug.exceptions import InternalServerError, NotFound
from exception.custom_exception import TokenException, NotExistException


def error_handler(app):
    @app.errorhandler(NotFound)
    def handle_not_found(e):
        """
        access with wrong url
        :param e: error object
        :return: error message and status code
        """

        return 'This url format is wrong. Insert the url formated : <127.0.0.1:5000/<naming list seperated by comma>', e.code

    @app.errorhandler(InternalServerError)
    def handle_sever_error(e):
        """
        internal error
        :param e: error object
        :return: error message and status code
        """

        return e.description, e.code

    @app.errorhandler(TokenException)
    def handle_token_error(e):
        """
        the access token is wrong or not found
        :param e: error object
        :return: error message and status code
        """

        return e.dev_error_message, e.status_code

    @app.errorhandler(NotExistException)
    def handle_token_error(e):
        """
        some repository name in endpoints doesn't exist
        :param e: error object
        :return: error message and status code
        """

        return e.dev_error_message, e.status_code
