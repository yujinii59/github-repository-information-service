class TokenException(Exception):
    def __init__(self):
        self.status_code = 401
        self.dev_error_message = \
            "<h2>GitHub Access Token Error</h2>" \
            "Check the github personal access token. <br>" \
            "If you didn't create an environment variable, please create it."


class NotExistException(Exception):
    def __init__(self):
        self.status_code = 406
        self.dev_error_message = "<h2>Repository name Error</h2>" \
                                 "Some repositories doesn't exist."
