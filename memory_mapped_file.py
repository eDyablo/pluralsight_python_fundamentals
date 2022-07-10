#!/usr/bin/env python3
import mmap as mm

with (
    open(__file__, mode="r") as file,
    mm.mmap(file.fileno(), 0, access=mm.ACCESS_READ) as mf,
):
    print(mf[24:-1].decode("utf-8"))
