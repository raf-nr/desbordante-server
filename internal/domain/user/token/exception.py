class ExpiredTokenSignatureException(Exception):

    def __init__(self):
        super().__init__("Token expired")


class InvalidTokenSignatureException(Exception):

    def __init__(self):
        super().__init__("Invalid token signature")


class DecodeTokenException(Exception):

    def __init__(self, message):
        super().__init__(message)


class InvalidTokenException(Exception):

    def __init__(self, message):
        super().__init__(message)


class InvalidTokenPayloadException(Exception):

    def __init__(self, message):
        super().__init__(message)
