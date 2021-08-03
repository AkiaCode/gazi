from gaji.route import Route
import typing


class App:
    def __init__(self):
        self.__routes = []
        self.__send = typing.Any
        self.__receive = typing.Any

    async def __call__(self, scope, receive, send) -> None:
        assert scope["type"] == "http"
        self.__send = send
        self.__receive = receive

        for route in self.__routes:

            if (
                route["class_name"] == "_"
                and "/" == scope["path"]
                and route["method"] == scope["method"]
            ):

                func = typing.Any
                if route["func_name"] == "__render__":
                    func = route["func"](scope)
                else:
                    RuntimeError("function __render__ not found")

                await self.__send_body(
                    func.status, route["method"], func.cType, func.data, func.headers
                )
                break

            elif (
                "/" + route["class_name"].lower() == scope["path"].lower()
                or "/" + route["class_name"].lower() + "/" == scope["path"].lower()
                and route["method"] == scope["method"]
            ):
                if route["func_name"] == "__render__":
                    func = route["func"](scope)
                else:
                    RuntimeError("function __render__ not found")

                await self.__send_body(
                    func.status, route["method"], func.cType, func.data, func.headers
                )
                break

            elif (
                "/" + route["class_name"].lower() + "/" + route["func_name"].lower()
                == scope["path"].lower()
                or "/"
                + route["class_name"].lower()
                + "/"
                + route["func_name"].lower()
                + "/"
                == scope["path"].lower()
                and route["method"] == scope["method"]
            ):

                func = route["func"](scope)

                await self.__send_body(
                    func.status, route["method"], func.cType, func.data, func.headers
                )
                break
            else:
                continue

    def handlers(self, routes=[]):
        for route in routes:
            self.__routes.extend(Route().register(route))

    async def __send_body(
        self, status=404, method="GET", cType="text/plain", body="NOT FOUND", headers=[]
    ):
        # [[b'content-type', b'text/html'], headers]
        headers.append([b"content-type", bytes(cType + "; charset=utf-8", "utf-8")])

        await self.__send(
            {
                "type": "http.response.start",
                "status": status,
                "method": method,
                "headers": headers,
            }
        )

        await self.__send(
            {
                "type": "http.response.body",
                "body": bytes(body, "utf-8"),
            }
        )

        await self.__receive()
