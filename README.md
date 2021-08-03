# gazi
A lightweight, class-based, easy-to-use ASGI framework

### Docs

* main.py
```python
from gazi import App
from home import _ as Home
from api import API

app = App()

app.handlers([Home, API])
```

* home.py
```python
from gazi.route import method
from gazi.response import HtmlResponse, Response

# Path: /*
class _:
    def __init__(self) -> None:
        pass

    # Path: /
    @method.GET
    def __render__(self) -> Response:
        return HtmlResponse("<h1>Hello, world!</h1>")
```

* api.py
```python
from gazi.response import HtmlResponse, Response
from gazi.request import Request
from gazi.route import method

# Path: /api/*
class API:
    def __init__(self) -> None:
        pass

    # Path: /api
    @method.GET
    def __render__(self) -> Response:
        return Response("API")

    # Path: /api/hello
    @method.GET
    def hello(self, request: Request) -> Response:
        return HtmlResponse(
            f"<h1>Hello world, Username: {request.query('name')}</h1>", # data
            {"test1": "test", "asd": "a"}, # headers
        )

    # Path: /api/bye?name=test
    @method.POST
    def bye(self, request: Request) -> Response:
        return HtmlResponse(f"<h1>Bye world, Username: {request.query('name')}</h1>")
```