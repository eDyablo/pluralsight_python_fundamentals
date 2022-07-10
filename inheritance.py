from tracer import Tracer

traced = Tracer()


class Base:
    @traced
    def __init__(self):
        pass

    @traced
    def f(self):
        pass


class Sub(Base):
    @traced
    def __init__(self):
        super().__init__()

    @traced
    def f(self):
        pass


class Stream:
    @traced
    def __init__(self):
        pass


class ReadStream(Stream):
    @traced
    def __init__(self):
        super().__init__()


class WriteStream(Stream):
    @traced
    def __init__(self):
        super().__init__()


class ReadWriteStream(ReadStream, WriteStream):
    @traced
    def __init__(self):
        super().__init__()
