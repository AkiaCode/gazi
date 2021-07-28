import uvicorn
from examples.pages.home import Home
from examples.pages.api import API
from gaji.route import Route
from gaji import App

app = App()

app.route(Route().register(API))
app.route(Route().register(Home))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

# uvicorn main:app