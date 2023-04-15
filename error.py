from werkzeug.exceptions import BadRequest, Forbidden, NotFound, RequestTimeout, InternalServerError
from exception.custom_exception import TokenException, NotExistException


def error_handler(app):
    @app.errorhandler(BadRequest)
    def handle_bad_request(e):
        """
        Raise if the browser sends something to the application or server cannot handle.
        :param e: error object
        :return: error message and status code
        """

        return "<h2>Bad Request</h2>" + e.description, e.code

    @app.errorhandler(Forbidden)
    def handle_permission_error(e):
        """
        no permission for the requested resource
        :param e: error object
        :return: error message and status code
        """

        return "<h2>Permission Denied</h2>" + e.description, e.code

    @app.errorhandler(NotFound)
    def handle_not_found(e):
        """
        access with wrong url
        :param e: error object
        :return: error message and status code
        """

        return "<h2>Not Found</h2>" \
               "This url format is wrong.<br>" \
               "Insert the url formated : http://127.0.0.1:5000/api/repository-name1,repository-name2,...", e.code

    @app.errorhandler(RequestTimeout)
    def handle_timeout(e):
        """
        timeout
        :param e: error object
        :return: error message and status code
        """

        return "<h2>Timeout</h2>" + e.description, e.code

    @app.errorhandler(InternalServerError)
    def handle_sever_error(e):
        """
        internal error
        :param e: error object
        :return: error message and status code
        """

        return "<h2>Server Error</h2>"+e.description, e.code

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
