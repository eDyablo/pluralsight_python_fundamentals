#!/usr/bin/env python3

from operator import mod
import sys


def read_series(filename):
    with open(filename, mode="rt", encoding="utf-8") as file:
        return [int(line.strip()) for line in file]


def main(filename):
    print(read_series(filename))


if __name__ == "__main__":
    main(sys.argv[1])
