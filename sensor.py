#!/usr/bin/env python3

import random
import datetime
from itertools import islice
import time


class Sensor:
    def __iter__(self):
        return self

    def __next__(self):
        return random.random()


def main():
    sensor_values = iter(Sensor())
    timestamps = iter(datetime.datetime.now, None)
    for ts, value in islice(zip(timestamps, sensor_values), 10):
        print(f"{ts}: {value}")
        time.sleep(1)


if __name__ == "__main__":
    main()
