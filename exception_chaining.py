#!/usr/bin/env python3

import traceback
from math import atan, degrees


class InclanationError(Exception):
    pass


def inclanation(dx, dy):
    try:
        return degrees(atan(dy / dx))
    except ZeroDivisionError as e:
        raise InclanationError("Slope can not be vertical") from e


def main():
    try:
        print(inclanation(0, 5))
    except InclanationError as e:
        traceback.print_tb(e.__traceback__)
        ts = traceback.format_tb(e.__traceback__)
        print(ts)


if __name__ == "__main__":
    main()
    print("Finished")
