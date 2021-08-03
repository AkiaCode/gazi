import typing


class App:
    def __init__(self):
        self.routes = []
        self.send = typing.Any
        self.receive = typing.Any

    async def __call__(self, scope, receive, send) -> None:
        assert scope["type"] == "http"
        self.send = send
        self.receive = receive

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

                await self.send_body(
                    func.to_status(), route["method"], func.to_cType(), func.to_data()
                )
                break

            elif "/" + route["class_name"].lower() == scope["path"].lower():
                if route["func_name"] == "__render__":
                    func = route["func"](scope)
                else:
                    RuntimeError("function __render__ not found")

                await self.send_body(
                    func.to_status(), route["method"], func.to_cType(), func.to_data()
                )
                break
            elif (
                "/" + route["class_name"].lower() + "/" + route["func_name"].lower()
                == scope["path"].lower()
            ):

                func = route["func"](scope)

                await self.send_body(
                    func.to_status(), route["method"], func.to_cType(), func.to_data()
                )
                break
            else:
                continue

    def route(self, routes):
        self.routes.extend(routes)

    async def send_body(self, status=200, method="GET", cType="text/plain", body=""):
        await self.send(
            {
                "type": "http.response.start",
                "status": status,
                "method": method,
                "headers": [
                    [b"content-type", bytes(cType, "utf-8")],
                ],
            }
        )

        await self.send(
            {
                "type": "http.response.body",
                "body": bytes(body, "utf-8"),
            }
        )

        await self.receive()
