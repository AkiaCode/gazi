import uvicorn
from examples.pages.home import _ as Home
from examples.pages.api import API
from gazi import App

app = App()

app.handlers([Home, API])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, headers=[("server", "gazi")])

# uvicorn main:app
