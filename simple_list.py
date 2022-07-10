from tracer import Tracer

traced = Tracer()


class SimpleList:
    def __init__(self, items=()):
        self._items = list(items)

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"SimpleList({self._items})"

    @traced
    def add(self, item):
        self._items.append(item)
        return self

    def sort(self):
        self._items.sort()


class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(items)
        self.sort()

    @traced
    def add(self, item):
        super().add(item)
        self.sort()
        return self

    def __repr__(self):
        return f"SortedList({list(self)})"


class IntList(SimpleList):
    def __init__(self, items=()):
        for i in items:
            self._validate_item(i)
        super().__init__(items)

    def _validate_item(self, item):
        if not isinstance(item, int):
            raise TypeError(f"{type(self).__name__} only supports integer values")

    @traced
    def add(self, item):
        self._validate_item(item)
        super().add(item)
        return self

    def __repr__(self):
        return "IntList({!r})".format(list(self))


class SortedIntList(IntList, SortedList):
    def __repr__(self):
        return "SortedIntList({!r})".format(list(self))
