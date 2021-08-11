from gazi.response import FormDataResponse, HtmlResponse, Response
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

    @method.POST
    def test(self, request: Request) -> Response:
        return FormDataResponse([{ 'file': './public/assets/logo.svg', 'filename': 'logo.svg', 'name': 'logo' }])


    # /api/bye
    @method.GET
    def bye(self, request: Request) -> Response:
        print(request.headers('host'))
        return HtmlResponse(f"<h1>Bye world, Username: {request.query('name')}</h1>")
