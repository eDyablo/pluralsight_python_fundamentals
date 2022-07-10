#!/usr/bin/env python3

import mmap
from pprint import pp
from binascii import hexlify


class Vector:
    __slots__ = ["_mem"]

    def __init__(self, mem_float32):
        self._mem = mem_float32

    @property
    def x(self):
        return self._mem[0]

    @property
    def y(self):
        return self._mem[1]

    @property
    def z(self):
        return self._mem[2]

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


class Color:
    __slots__ = ["_mem"]

    def __init__(self, mem_uint16):
        self._mem = mem_uint16

    @property
    def red(self):
        return self._mem[0]

    @property
    def green(self):
        return self._mem[1]

    @property
    def blue(self):
        return self._mem[2]

    def __repr__(self):
        return f"Color({self.red}, {self.green}, {self.blue}"


class Vertex:
    __slots__ = ["position", "color"]

    def __init__(self, position, color):
        self.position = position
        self.color = color

    def __repr__(self):
        return "Vertex({!r}, {!r})".format(self.position, self.color)


def make_colored_vertex(mem_vertex):
    mem_position = mem_vertex[0:12].cast("f")
    mem_color = mem_vertex[12:18].cast("H")
    return Vertex(Vector(mem_position), Color(mem_color))


def main():
    with open("colorpoints.bin", "rb") as file:
        with mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as buffer:

            print(f"buffer: {len(buffer)} bytes")

            indices = " ".join(str(n).zfill(2) for n in range(len(buffer)))
            print(indices)

            hex_buffer = hexlify(buffer).decode("ascii")
            hex_pairs = " ".join(
                hex_buffer[i : i + 2] for i in range(0, len(hex_buffer), 2)
            )
            print(hex_pairs)

            mem = memoryview(buffer)

            VERTEX_SIZE = 18
            VERTEX_STRIDE = VERTEX_SIZE + 2

            vertex_mems = (
                mem[i : i + VERTEX_SIZE] for i in range(0, len(mem), VERTEX_STRIDE)
            )
            vertices = [make_colored_vertex(mem_vertex) for mem_vertex in vertex_mems]

            pp(vertices)

            del vertices
            del mem


if __name__ == "__main__":
    main()
