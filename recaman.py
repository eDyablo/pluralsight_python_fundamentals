#!/usr/bin/env python3

from itertools import count, islice
import sys


def sequence():
    """Generate Recaman's sequence."""
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c


def write_sequence(filename, num):
    """Write Recaman's sequence to a text file."""
    with open(filename, mode="wt", encoding="utf-8") as file:
        file.writelines("{0}\n".format(n) for n in islice(sequence(), num + 1))


if __name__ == "__main__":
    write_sequence(filename=sys.argv[1], num=int(sys.argv[2]))
