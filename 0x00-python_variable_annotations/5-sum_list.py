#!/usr/bin/env python3
"""
A type-annotated function that takes a list of
floats as arguments and returns their sum as float
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """This returns their sum as a float"""
    return float(sum(input_list))
