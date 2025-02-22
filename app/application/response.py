from typing import Any

class Response:
    def __init__(self, status_code: int, message: str, data: Any):
        self.status_code = status_code
        self.message = message
        self.data = data

    def __repr__(self):
        return '<%s (%s, %s, %s)>' % (
            self.__class__.__name__, self.status_code, self.message, self.data
        )