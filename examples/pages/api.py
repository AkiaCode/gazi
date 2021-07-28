from gaji.route import method

# /api/*
class API:
    def __init__(self) -> None:
        pass
    # 404: /api/*
    def __404__(self) -> str:
        return "404"

    #  /api/hello/{name:str}
    @method.GET
    def hello(self, name: str) -> str:
        return f"Hello world, Username: {name}"

    # /api/bye/{name}
    @method.POST
    def bye(self, name) -> str:
        return f"Bye {name}"
