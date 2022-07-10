from argparse import ArgumentError
import functools

from click import Argument


def check_non_negative(index):
    def decorator(f):
        @functools.wraps(f)
        def wraper(*args):
            if args[index] < 0:
                raise ValueError("Argument {} must be non-negative".format(index))
            return f(*args)

        return wraper

    return decorator


@check_non_negative(1)
def create_list(value, size):
    """Create list from value by repeating it."""
    return [value] * size
