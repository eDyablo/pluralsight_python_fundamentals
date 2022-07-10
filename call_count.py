class CallCount:
    def __init__(self, f):
        self._f = f
        self._count = 0

    def __call__(self, *args, **kwds):
        self._count += 1
        return self._f(*args, **kwds)


@CallCount
def hello(name):
    print("hello, {}".format(name))
