#!/usr/bin/env python3


class ChessCoordinate:
    _interned = {}

    def __new__(cls, file, rank):
        key = (file, rank)
        if key not in cls._interned:
            obj = super().__new__(cls)
            obj._file = file
            obj._rank = rank
            cls._interned[key] = obj
        return cls._interned[key]

    @property
    def file(self):
        return self._file

    @property
    def rank(self):
        return self._rank

    def __repr__(self):
        return f"{self.__class__.__name__}({self.file}, {self.rank})"

    def __str__(self):
        return f"{self.file}{self.rank}"


def main():
    white_queen = ChessCoordinate("d", 4)
    print(white_queen)


if __name__ == "__main__":
    main()
