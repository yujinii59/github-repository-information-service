class TokenException(Exception):
    def __init__(self):
        self.status_code = 600
        self.dev_error_message = "Check github personal access token! \nIf you didn't create an environment variable, please create it!"


