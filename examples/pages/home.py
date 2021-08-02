from gaji.request import Request
from gaji.route import method
from gaji.response import HtmlResponse, Response

# /
class _:
    def __init__(self) -> None:
        pass

    # /
    @method.GET
    def __render__(self) -> Response:
        return HtmlResponse("<h1>Hello, world!</h1>")
