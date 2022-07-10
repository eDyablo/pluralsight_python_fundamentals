import functools


def escape_unicode(f):
    @functools.wraps(f)
    def escape(*args, **kwargs):
        return ascii(f(*args, **kwargs))

    return escape


@escape_unicode
def ukrainian_city():
    return "Одеса"
