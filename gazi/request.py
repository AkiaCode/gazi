class Request(object):
    def __init__(self, scope):
        self.__scope = scope

    def query(self, key=None):
        if "query_string" in self.__scope:
            if key is None:
                return self.query_string
            else:
                for query_string in self.query_string.split("&"):
                    if key in query_string:
                        return query_string.replace(key + "=", "")
        else:
            return None

    def headers(self, key=None):
        if "headers" in self.__scope:
            if key is None:
                return self.__scope['headers']
            else:
                for header in self.__scope['headers']:
                    if key == str(header[0], 'utf-8'):
                        return str(header[1], 'utf-8')
        else:
            return None

    @property
    def query_string(self) -> str:
        return str(self.__scope["query_string"], "utf-8")

    @property
    def root_path(self):
        return self.__scope["root_path"]

    @property
    def client(self):
        return self.__scope["client"]

    @property
    def server(self):
        return self.__scope["server"]

    @property
    def http_version(self):
        return self.__scope["http_version"]

    @property
    def raw_path(self):
        return self.__scope["raw_path"]

    @property
    def type(self) -> str:
        return self.__scope["type"]

    @property
    def path(self) -> str:
        return self.__scope["path"]

    @property
    def scheme(self) -> str:
        return self.__scope["scheme"]

    @property
    def method(self) -> str:
        return self.__scope["method"]

    @property
    def body(self) -> str:
        return self.__scope['body'] or None

    @property
    def files(self) -> dict:
        boundary = self.headers("content-type").split("=")[1]
        splited = self.body[: len(self.body) - len(boundary) - 6].split(
            ("--" + boundary + "\r\n").encode("utf8")
        )
        data = {}
        for content in splited[1:]:
            splited = content.split(b"\r\n")
            disposition = splited[0].decode("utf8")
            split_by_semi = disposition.split(";")
            name = split_by_semi[1][7 : len(split_by_semi[1]) - 1]
            result = {}
            if len(split_by_semi) > 2:
                filename = split_by_semi[2][11 : len(split_by_semi[2]) - 1]
                result["filename"] = filename

            value = b"\r\n".join(splited[splited.index(b'') + 1 : len(splited) - 1])
            try:
                value = value.decode("utf8")
            except UnicodeDecodeError:
                pass
            result["content"] = value
            data[name] = result
        return data