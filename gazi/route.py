from gazi.request import Request
import typing


class Route:
    def __init__(self) -> None:
        pass

    def register(self, class_name: typing.Any) -> typing.Any:
        class_func_names = []
        for func_name in dir(class_name):
            if hasattr(getattr(class_name, func_name), "name") == False:
                RuntimeError("must use @method.GET decorator")

            if func_name.startswith("__") and func_name.endswith("__"):
                if "render" in func_name:
                    class_func_names.append(
                        {
                            "class_name": class_name.__name__,
                            "func_name": func_name,
                            "func": getattr(class_name, func_name),
                            "method": getattr(class_name, func_name).name,
                        }
                    )
                continue

            """
            annotations = []

            if hasattr(getattr(class_name, func_name), "__annotations__"):
                annotations = getattr(class_name, func_name).__annotations__
                if len(annotations) == 1 and "return" in annotations:
                    annotations = []

            varnames = []

            if hasattr(getattr(class_name, func_name), "__code__"):
                for co_varname in getattr(class_name, func_name).__code__.co_varnames:
                    if co_varname == "self":
                        continue
                    if co_varname in annotations:
                        varnames.append(
                            {"name": co_varname, "type": annotations[co_varname]}
                        )
                    else:
                        varnames.append({"name": co_varname, "type": None})
            """

            class_func_names.append(
                {
                    "class_name": class_name.__name__,
                    "func_name": func_name,
                    "func": getattr(class_name, func_name),
                    # "parameter": varnames,
                    "method": getattr(class_name, func_name).name,
                }
            )

        return class_func_names


class method(Route):
    class GET(object):
        def __init__(self, func):
            self.name = "GET"
            self.func = func

        def __call__(self, args):
            if len(self.func.__code__.co_varnames) == 1:
                return self.func(self)
            else:
                args = Request(args)
                return self.func(self, args)

    class POST(object):
        def __init__(self, func):
            self.name = "POST"
            self.func = func

        def __call__(self, args):
            if len(self.func.__code__.co_varnames) == 1:
                return self.func(self)
            else:
                args = Request(args)
                return self.func(self, args)
