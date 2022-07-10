#!/usr/bin/env python3

l = [(x, y) for x in range(5) for y in range(5)]
print(l)

l = [[(x, y) for y in range(5)] for x in range(5)]
print(l)

sizes = ['small', 'medium', 'large']
colors = ['red', 'green', 'blue', 'purple']
print(list(map(lambda f,s: f"{f} {s}", sizes, colors)))

import itertools
print([f"{n} x {s} {c}" for n, s, c in zip(itertools.count(start=1), sizes, colors)])

import datetime
print([f"{n}: {t}" for n, t in zip(range(1, 6), iter(datetime.datetime.now, None))])