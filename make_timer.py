import time
from tkinter.messagebox import NO


def make_timer():
    last_called = None

    def elapsed():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            last_called = now
            return None
        diff = now - last_called
        last_called = now
        return diff

    return elapsed
