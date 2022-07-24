#!/usr/bin/env python3

from planet import Planet


def main():
    pluto = Planet(
        "Pluto",
        radius_metres=1184e3,
        mass_kilograms=1.305e22,
        orbital_period_seconds=7816012992,
        surface_temperature_kelvin=55,
    )


if __name__ == "__main__":
    main()
