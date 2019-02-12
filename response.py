class Response:

    def __init__(self, content, statusCode):
        self.content = content
        self.statusCode = statusCode

    def onError(self):
        return "Error: " + self.statusCode