class NoMatch(Exception):
    def __init__(self):
        super().__init__("Invalid gamer credentials")

class AuthError(Exception):
    def __init__(self):
        super().__init__("Invalid auth")

class MissingGamer(Exception):
    def __init__(self):
        super().__init__("Invalid gamer id")

class TokenMismatch(Exception):
    def __init__(self):
        super().__init__("Invalid token")

class ValidationException(Exception):
    def __init__(self):
        super().__init__("One of the arguments is invalid")