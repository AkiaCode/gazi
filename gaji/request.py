class Request:
    def __init__(self, scope):
        self.scope = scope
        self.type = str(self.scope["type"])
        self.path = str(self.scope["path"])
        self.scheme = str(self.scope["scheme"])
        self.method = str(self.scope["method"])
        self.raw_path = str(self.scope["raw_path"])
        self.http_version = str(self.scope["http_version"])
        self.server = self.scope["server"]
        self.client = self.scope["client"]
        self.headers = self.scope["headers"]
        self.root_path = self.scope["root_path"]
        self.query_string = str(self.scope["query_string"], "utf-8")

    def query(self, key=None):
        if "query_string" in self.scope:
            if key is None:
                return self.query_string
            else:
                for query_string in self.query_string.split("&"):
                    if key in query_string:
                        return query_string.replace(key + "=", "")
        else:
            return None
