class NoMatchError(Exception):
    def __init__(self):
        super().__init__("Invalid gamer credentials")