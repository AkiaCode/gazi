import typing


class App:
    def __init__(self):
        self.routes = []

    async def __call__(self, scope, receive, send) -> None:
        assert scope['type'] == 'http'

        for route in self.routes:

            if route['class_name'].lower() == 'Home'.lower() and '/' == scope['path'].lower():

                func = typing.Any
                if route['func_name'] == 'render':
                    func = route['func'](self)


                await send({
                    'type': 'http.response.start',
                    'status': 200,
                    'method': route['method'],
                    'headers': [
                        [b'content-type', b'text/html'],
                    ],
                })

                await send({
                    'type': 'http.response.body',
                    'body': bytes(func, 'utf-8'),
                    'headers': [
                        [b'content-type', b'text/html; charset=utf-8'],
                        [b'content-length', bytes(str(len(func)), 'utf-8')]
                    ]
                })

                await receive()
                break

            elif '/' + route['class_name'].lower()  + '/' + route['func_name'].lower() == scope['path'].lower():

                func = route['func'](str(scope['query_string'], 'utf-8').replace('name=', ''))

                await send({
                    'type': 'http.response.start',
                    'status': 200,
                    'method': route['method'],
                    'headers': [
                        [b'content-type', b'text/plain'],
                    ],
                })

                await send({
                    'type': 'http.response.body',
                    'body': bytes(func, 'utf-8'),
                })

                await receive()
                break

            else:
                continue

    def route(self, routes):
        self.routes.extend(routes)
