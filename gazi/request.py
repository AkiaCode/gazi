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
                    if key in header:
                        return str(header[key], 'utf-8')
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