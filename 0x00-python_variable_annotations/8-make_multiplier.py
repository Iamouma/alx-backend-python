#!/usr/bin/env python3
"""
A type-annotated function that takes a float multiplier as
argument and returns a function that multiplies a float by the multiplier.
"""


import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """This returns a function that muiltiplies a float by multiplier"""
    def float_multiply(x: float) -> float:
        return multiplier * x

    return float_multiply
