#!/usr/bin/env python3
"""
A type-annotated function that takes a list of intergers
and floats and returns their sum.
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """Returns the sum of the list as a float"""
    return float(sum(mxd_lst))
