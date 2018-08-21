from functools import wraps


def redirect_exception(source, target):
    """ Redirect an exception type of `source` type to `target` type.

    :param Exception source: Type of exception that will be redirected.
    :param Exception target: Type of exception that the source will be redirected to.
    """

    def exception_checker(func):
        @wraps(func)
        def wrapper():
            try:
                func()
            except source as e:
                raise target(e)

        return wrapper

    return exception_checker
