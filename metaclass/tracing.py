from curses import meta


class TracingMeta(type):
    @classmethod
    def __prepare__(metacls, name, bases, **kwds):
        namespace = super().__prepare__(name, bases, **kwds)
        return namespace

    def __new__(metacls, name, bases, namespace, **kwds):
        cls = super().__new__(metacls, name, bases, namespace, **kwds)
        return cls

    def __init__(cls, name, bases, namespace, **kwds):
        super().__init__(name, bases, namespace, **kwds)

    def metamethod(cls):
        print("TracingMeta.metamethod")
        print("cls =", cls)
        print()

    def __call__(cls, *args, **kwds):
        obj = super().__call__(*args, **kwds)
        return obj


class TracingClass(metaclass=TracingMeta):
    def __new__(cls, *args, **kwds):
        obj = super().__new__(cls)
        return obj

    def __init__(self, *args, **kwds):
        print("TracingClas.__init__(self, *args, **kwds)")
        print("  self=", self)
        print("  args=", args)
        print("  kwds=", kwds)
        print()
