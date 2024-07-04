#!/usr/bin/env python3
"""
A type-annotated function that takes a string and int OR
float as arguments and returns a tuple.
"""


import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    This returns a tuple of the string and sauare of
    v as float
    """
    return (k, float(v * v))
