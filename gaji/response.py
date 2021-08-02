class Response:
    def __init__(self, data, status=200, cType="text/plain"):
        self.status = status
        self.data = data
        self.cType = cType

    def to_data(self) -> str:
        return self.data

    def to_cType(self) -> str:
        return self.cType

    def to_status(self) -> int:
        return self.status


class HtmlResponse(Response):
    def __init__(self, data, status=200):
        super().__init__(data, status, "text/html")


class JsonResponse(Response):
    def __init__(self, data, status=200):
        super().__init__(data, status, "application/json")
