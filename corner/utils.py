import functools

__all__ = ['defaults']


def defaults(**default_kwargs):
    def wrapper_factory(func):
        @functools.wraps(func)
        def wrapper(**kwargs):
            for key, make_default in default_kwargs.items():
                if kwargs.get(key) is None:
                    kwargs[key] = make_default()
            return func(**kwargs)
        return wrapper
    return wrapper_factory

