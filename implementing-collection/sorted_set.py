from bisect import bisect_left
from collections.abc import Sequence
from itertools import chain


class SortedSet(Sequence):
    def __init__(self, items=None):
        self._items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        index = bisect_left(self._items, item)
        return index != len(self._items) and self._items[index] == item

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return (
            SortedSet(self._items[index])
            if isinstance(index, slice)
            else self._items[index]
        )

    def __repr__(self):
        return "SortedSet({})".format(repr(self._items) if self._items else "")

    def __eq__(self, rhs):
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items == rhs._items

    def __ne__(self, rhs):
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items != rhs._items

    def count(self, item):
        return int(item in self)

    def index(self, item):
        index = bisect_left(self._items, item)
        if index != len(self._items) and self._items[index] == item:
            return index
        raise ValueError(f"{repr(item)} not found")

    def __add__(self, rhs):
        return SortedSet(chain(self._items, rhs._items))

    def __mul__(self, rhs):
        return self if rhs > 0 else SortedSet()

    def __rmul__(self, lhs):
        return self * lhs