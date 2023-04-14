class TokenException(Exception):
    def __init__(self):
        self.status_code = 600
        self.dev_error_message = \
            "Check the github personal access token. \nIf you didn't create an environment variable, please create it."


class NotExistException(Exception):
    def __init__(self):
        self.status_code = 601
        self.dev_error_message = "Some repositories doesn't exist"
