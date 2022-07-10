import functools


class Tracer:
    def __init__(self):
        self.enabled = True
        self._indent = 0

    def __call__(self, f):
        @functools.wraps(f)
        def traced(*args, **kwargs):
            if self.enabled:
                print(f"{' ' * self._indent}Calling {f}")
            try:
                self._indent += 1
                return f(*args, **kwargs)
            finally:
                self._indent -= 1

        return traced


tracer = Tracer()


@tracer
def rotate_list(l):
    return l[1:] + [l[0]]
