import typing


class App:
    def __init__(self):
        self.routes = []

    async def __call__(self, scope, receive, send) -> None:
        assert scope["type"] == "http"

        for route in self.routes:

            if (
                route["class_name"].lower() == "_".lower()
                and "/" == scope["path"].lower()
            ):

                func = typing.Any
                if route["func_name"] == "__render__":
                    func = route["func"](scope)
                else:
                    RuntimeError("function __render__ not found")

                await send(
                    {
                        "type": "http.response.start",
                        "status": func.to_status(),
                        "method": route["method"],
                        "headers": [
                            [b"content-type", bytes(func.to_cType(), "utf-8")],
                        ],
                    }
                )

                await send(
                    {
                        "type": "http.response.body",
                        "body": bytes(func.to_data(), "utf-8"),
                    }
                )

                await receive()
                break

            elif "/" + route["class_name"].lower() == scope["path"].lower():
                if route["func_name"] == "__render__":
                    func = route["func"](scope)
                else:
                    RuntimeError("function __render__ not found")

                await send(
                    {
                        "type": "http.response.start",
                        "status": func.to_status(),
                        "method": route["method"],
                        "headers": [
                            [b"content-type", bytes(func.to_cType(), "utf-8")],
                        ],
                    }
                )

                await send(
                    {
                        "type": "http.response.body",
                        "body": bytes(func.to_data(), "utf-8"),
                    }
                )

                await receive()
                break
            elif (
                "/" + route["class_name"].lower() + "/" + route["func_name"].lower()
                == scope["path"].lower()
            ):

                func = route["func"](scope)

                await send(
                    {
                        "type": "http.response.start",
                        "status": func.to_status(),
                        "method": route["method"],
                        "headers": [
                            [b"content-type", bytes(func.to_cType(), "utf-8")],
                        ],
                    }
                )

                await send(
                    {
                        "type": "http.response.body",
                        "body": bytes(func.to_data(), "utf-8"),
                    }
                )

                await receive()
                break
            else:
                continue

    def route(self, routes):
        self.routes.extend(routes)
