class KeywordsOnlyMeta(type):
    def __call__(cls, *args, **kwds):
        if args:
            raise TypeError(
                f"Constructor of class {cls} does not accept positional arguments"
            )
        return super().__call__(cls, **kwds)


class ConstrainedToKeywords(metaclass=KeywordsOnlyMeta):
    def __init__(self, *args, **kwds):
        print("args =", args)
        print("kwds =", kwds)
