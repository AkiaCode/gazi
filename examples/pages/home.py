from gazi.route import method
from gazi.response import HtmlResponse, Response

# /
class _:
    def __init__(self) -> None:
        pass

    # /
    @method.GET
    def __render__(self) -> Response:
        return HtmlResponse("<h1>Hello, world!</h1>")
