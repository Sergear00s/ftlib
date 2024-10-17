

class Error_response(Exception):
    def __init__(self, message):
        super().__init__(message)


class Error_auth(Exception):
    def __init__(self, message):
        super().__init__(message)


class RateLimit(Exception):
    def __init__(self, message):
        super().__init__(message)


