from gaji.response import HtmlResponse, Response
from gaji.request import Request
from gaji.route import method

# /api/*
class API:
    def __init__(self) -> None:
        pass

    #  /api
    @method.GET
    def __render__(self) -> Response:
        return Response("API")

    #  /api/hello
    @method.GET
    def hello(self, request: Request) -> Response:
        return HtmlResponse(f"<h1>Hello world, Username: {request.query('name')}</h1>")

    # /api/bye
    @method.GET
    def bye(self, request: Request) -> Response:
        return HtmlResponse(f"<h1>Bye world, Username: {request.query('name')}</h1>")
