from gazi.response import HtmlResponse, Response
from gazi.request import Request
from gazi.route import method

# /api/*
class API:
    def __init__(self) -> None:
        pass

    #  /api
    @method.GET
    def __render__(self) -> Response:
        return Response("API")

    #  /api/hello
    @method.POST
    def hello(self, request: Request) -> Response:
        print(request.body)
        return HtmlResponse(
            f"<h1>Hello world, Username: {None}</h1>",
            {"test1": "test", "asd": "a"},
        )

    # /api/bye
    @method.GET
    def bye(self, request: Request) -> Response:
        return HtmlResponse(f"<h1>Bye world, Username: {request.query('name')}</h1>")
