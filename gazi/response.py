class Response:
    def __init__(self, data, headers=[], status=200, cType="text/plain"):
        self.__data = data
        self.__headers = headers
        self.__status = status
        self.__cType = cType

    @property
    def headers(self):
        bytes_headers = []

        if len(self.__headers) == 0:
            return bytes_headers
        else:
            for header in self.__headers.items():
                bytes_headers.append(
                    [bytes(header[0], "utf-8"), bytes(header[1], "utf-8")]
                )

        return bytes_headers

    @property
    def data(self) -> str:
        return self.__data

    @property
    def cType(self) -> str:
        return self.__cType

    @property
    def status(self) -> int:
        return self.__status


class HtmlResponse(Response):
    def __init__(self, data, headers=[], status=200):
        super().__init__(data, headers, status, "text/html")


class JsonResponse(Response):
    def __init__(self, data, headers=[], status=200):
        super().__init__(data, headers, status, "application/json")
