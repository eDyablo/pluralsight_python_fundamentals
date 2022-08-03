#!/usr/bin/env python3

from ast import arg
import functools


def invariant(predicate):
    def invariant_checking_class_decorator(cls):
        method_names = [name for name, attr in vars(cls).items() if callable(attr)]
        for name in method_names:
            _wrap_method_with_invariant_checking_proxy(cls, name, predicate)
        return cls

    return invariant_checking_class_decorator


def _wrap_method_with_invariant_checking_proxy(cls, name, predicate):
    method = getattr(cls, name)
    assert callable(method)

    @functools.wraps(method)
    def invariant_checking_method_decorator(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        if not predicate(self):
            raise RuntimeError(
                "Class invariant {!r} violated for  {!r}".format(
                    predicate.__doc__, self
                )
            )
        return result

    setattr(cls, name, invariant_checking_method_decorator)


def my_decorated_class(cls):
    for name, attr in vars(cls).items():
        print(name)
    return cls


def not_below_absolute_zero(temperature):
    """Temperature not below absolute zero"""
    return temperature._kelvin >= 0


@invariant(not_below_absolute_zero)
class Temperature:
    def __init__(self, kelvin):
        self._kelvin = kelvin

    def get_kelvin(self):
        return self._kelvin

    def set_kelvin(self, value):
        self._kelvin = value

    @property
    def celsius(self):
        return self._kelvin - 273.15

    @celsius.setter
    def celsius(self, value):
        self._kelvin = value + 273.15


if __name__ == "__main__":
    t = Temperature(273)
    t.set_kelvin(0)
    t.celsius = -10
